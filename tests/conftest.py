import textwrap
from pathlib import Path

import pytest


@pytest.fixture
def write_csv(tmp_path: Path):
    """Фабрика создаёт csv-файл и возвращает его путь."""
    def _write_csv(name: str, content: str) -> Path:
        path = tmp_path / name
        path.write_text(textwrap.dedent(content).lstrip(), encoding="utf-8")
        return path
    return _write_csv


@pytest.fixture
def employees_two_files(write_csv):
    f1 = write_csv(
        "employees1.csv",
        """
        name,position,completed_tasks,performance,skills,team,experience_years
        David,Mobile Developer,36,4.6,Swift,Mobile,3
        Elena,Backend Developer,43,4.8,Java,API,4
        """,
    )
    f2 = write_csv(
        "employees2.csv",
        """
        name,position,completed_tasks,performance,skills,team,experience_years
        Tom,Backend Developer,49,4.9,Go,API,7
        Julia,QA Engineer,38,4.5,Playwright,Testing,3
        """,
    )
    return f1, f2


@pytest.fixture
def performance_report():
    from reporting.performance import PerformanceByPositionReport
    return PerformanceByPositionReport()
