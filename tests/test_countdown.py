"""Tests for scripts/countdown.py."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = REPO_ROOT / "scripts" / "countdown.py"

sys.path.insert(0, str(REPO_ROOT / "scripts"))

import countdown  # noqa: E402


def run_script(*args: str) -> subprocess.CompletedProcess[str]:
    """Run the countdown script as a user would, from the command line."""
    return subprocess.run(
        [sys.executable, str(SCRIPT), *args],
        capture_output=True,
        text=True,
        cwd=REPO_ROOT,
        check=False,
    )


def test_counts_down_and_prints_liftoff(capsys: pytest.CaptureFixture[str]) -> None:
    assert countdown.main(["3"]) == 0
    assert capsys.readouterr().out == "3\n2\n1\nLiftoff!\n"


@pytest.mark.parametrize("bad_value", ["0", "-2", "abc", "1.5"])
def test_invalid_input_exits_with_code_2(
    bad_value: str, capsys: pytest.CaptureFixture[str]
) -> None:
    with pytest.raises(SystemExit) as excinfo:
        countdown.main([bad_value])
    assert excinfo.value.code == 2
    assert capsys.readouterr().out == ""


def test_help_mentions_usage_and_exits_zero() -> None:
    result = run_script("--help")
    assert result.returncode == 0
    assert "usage:" in result.stdout
    assert "N" in result.stdout


def test_script_prints_countdown_and_liftoff() -> None:
    result = run_script("2")
    assert result.returncode == 0
    assert result.stdout == "2\n1\nLiftoff!\n"


def test_script_rejects_invalid_input_with_exit_code_2() -> None:
    result = run_script("0")
    assert result.returncode == 2
    assert result.stdout == ""
    assert "error" in result.stderr


def test_script_rejects_non_integer_with_exit_code_2() -> None:
    result = run_script("not-a-number")
    assert result.returncode == 2
    assert result.stdout == ""
