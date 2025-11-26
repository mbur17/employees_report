import pytest


@pytest.mark.parametrize(
    "rows, expected",
    [
        pytest.param(
            [
                {"position": "Backend Developer", "performance": "4.8"},
                {"position": "Backend Developer", "performance": "4.9"},
                {"position": "QA Engineer", "performance": "4.5"},
            ],
            [
                ["Backend Developer", 4.85],
                ["QA Engineer", 4.5],
            ],
            id="basic-average-and-sort",
        ),
        pytest.param(
            [
                {"position": "Data Engineer", "performance": "4.7"},
                {"position": "Data Engineer", "performance": "4.7"},
            ],
            [
                ["Data Engineer", 4.7],
            ],
            id="same-values",
        ),
    ],
)
def test_performance_report_averages_and_sort(
    performance_report, rows, expected
):
    result = performance_report.build(rows)
    assert result == expected
