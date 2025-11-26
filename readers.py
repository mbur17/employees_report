import csv
import logging
from typing import Any, Dict, Generator, Iterable

logger = logging.getLogger(__name__)


def iter_rows(
    file_paths: Iterable[str]
) -> Generator[Dict[str, Any], None, None]:
    """Читает все переданные CSV-файлы и отдает строки как dict."""
    for path in file_paths:
        try:
            with open(path, newline="", encoding="utf-8") as csv_file:
                logger.info("Reading file: %s", path)
                reader = csv.DictReader(csv_file)
                for row in reader:
                    yield row
        except FileNotFoundError:
            logger.error("File not found: %s", path)
        except OSError as exc:
            logger.error("Cannot read %s: %s", path, exc)
