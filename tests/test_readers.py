from readers import iter_rows


def test_iter_rows_reads_valid_file(write_csv):
    csv_path = write_csv(
        "employees.csv",
        """
        name,position,performance
        Alice,Backend Developer,4.8
        Bob,QA Engineer,4.5
        """,
    )
    rows = list(iter_rows([str(csv_path)]))
    assert len(rows) == 2
    assert rows[0]["name"] == "Alice"
    assert rows[1]["position"] == "QA Engineer"


def test_iter_rows_logs_missing_file(tmp_path, caplog):
    missing = tmp_path / "no_such_file.csv"
    with caplog.at_level("ERROR"):
        rows = list(iter_rows([str(missing)]))
    assert rows == []
    assert any("File not found" in rec.getMessage() for rec in caplog.records)
