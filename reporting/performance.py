import logging
from collections import defaultdict
from typing import Any, Dict, Iterable, List

from reporting.base import BaseReport

logger = logging.getLogger(__name__)


class PerformanceByPositionReport(BaseReport):
    """Отчет средней эффективности по позициям."""
    name = "performance"
    headers = ["position", "performance"]

    def build(self, rows: Iterable[Dict[str, Any]]) -> List[List[Any]]:
        sums: Dict[str, float] = defaultdict(float)
        counts: Dict[str, int] = defaultdict(int)
        for row in rows:
            position = row.get("position")
            raw_perf = row.get("performance")
            if not position or raw_perf in (None, ""):
                logger.debug(
                    "Skipping row without position or performance: %r",
                    row
                )
                continue
            try:
                performance = float(raw_perf)
            except (TypeError, ValueError):
                logger.warning(
                    "Invalid performance value %r for position %r, skipping",
                    raw_perf,
                    position,
                )
                continue
            sums[position] += performance
            counts[position] += 1
        result: List[List[Any]] = []
        for position, total in sums.items():
            avg = total / counts[position]
            result.append([position, round(avg, 2)])
        result.sort(key=lambda row: row[1], reverse=True)
        return result
