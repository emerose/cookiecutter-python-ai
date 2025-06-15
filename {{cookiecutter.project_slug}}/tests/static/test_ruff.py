"""Test that code passes ruff checks."""

import subprocess
import sys
from pathlib import Path

import pytest


@pytest.mark.static
@pytest.mark.ruff
def test_ruff_format():
    """Test that code is properly formatted."""
    result = subprocess.run(
        [sys.executable, "-m", "ruff", "format", "--check", "."],
        capture_output=True,
        text=True,
        cwd=Path(__file__).parent.parent.parent,
    )

    if result.returncode != 0:
        pytest.fail(f"Ruff format check failed:\n{result.stdout}\n{result.stderr}")


@pytest.mark.static
@pytest.mark.ruff
def test_ruff_lint():
    """Test that code passes linting."""
    result = subprocess.run(
        [sys.executable, "-m", "ruff", "check", "."],
        capture_output=True,
        text=True,
        cwd=Path(__file__).parent.parent.parent,
    )

    if result.returncode != 0:
        pytest.fail(f"Ruff lint check failed:\n{result.stdout}\n{result.stderr}")
