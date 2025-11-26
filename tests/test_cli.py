import main


def test_cli_full_flow(employees_two_files, capsys):
    f1, f2 = employees_two_files
    exit_code = main.main(
        [
            "--files",
            str(f1),
            str(f2),
            "--report",
            "performance",
        ]
    )
    out = capsys.readouterr().out
    assert exit_code == 0
    assert "position" in out
    assert "performance" in out
    assert "Backend Developer" in out
    assert "4.85" in out
