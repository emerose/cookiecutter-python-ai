"""Test that code passes pyright type checking."""

import subprocess
import sys
from pathlib import Path

import pytest


@pytest.mark.static
@pytest.mark.pyright
def test_pyright():
    """Test that code passes pyright type checking."""
    result = subprocess.run(
        [sys.executable, "-m", "pyright"],
        capture_output=True,
        text=True,
        cwd=Path(__file__).parent.parent.parent,
    )

    if result.returncode != 0:
        pytest.fail(f"Pyright type check failed:\n{result.stdout}\n{result.stderr}")
