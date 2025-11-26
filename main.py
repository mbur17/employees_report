import argparse
import logging
from typing import Any, Iterable, List

from tabulate import tabulate

from readers import iter_rows
from reporting import REPORTS

logger = logging.getLogger(__name__)


def parse_args(argv: Iterable[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate reports from employee CSV files",
    )
    parser.add_argument(
        "--files",
        nargs="+",
        required=True,
        help="Paths to CSV files (one or more)",
    )
    parser.add_argument(
        "--report",
        required=True,
        choices=REPORTS.keys(),
        help="Report name. Available: %(choices)s",
    )
    return parser.parse_args(list(argv) if argv is not None else None)


def print_table(headers: List[str], rows: List[List[Any]]) -> None:
    """Печатает отчет в виде таблицы в stdout."""
    if not rows:
        logger.info("No data to display")
        return
    table = tabulate(rows, headers=headers, showindex=1, tablefmt="simple")
    print(table)
    return


def main(argv: Iterable[str] | None = None) -> int:
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s:%(name)s:%(message)s",
    )
    args = parse_args(argv)
    logger.info("Selected report: %s", args.report)
    logger.info("Input files: %s", ", ".join(args.files))
    report = REPORTS[args.report]
    rows = list(iter_rows(args.files))
    report_rows = report.build(rows)
    print_table(report.headers, report_rows)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
