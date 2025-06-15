"""Global pytest configuration and fixtures."""

import os
import sys
from collections.abc import Iterator
from pathlib import Path
from typing import Any

import pytest
from _pytest.config import Config
from _pytest.python import Function

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))


def pytest_configure(config: Config) -> None:
    """Register custom markers."""
    config.addinivalue_line(
        "markers",
        "check: marks tests as part of check suite (unit + integration + static)",
    )
    config.addinivalue_line("markers", "all: marks tests as part of all test suite")
    config.addinivalue_line("markers", "static: marks tests as static analysis")
    config.addinivalue_line("markers", "unit: marks tests as unit tests")
    config.addinivalue_line("markers", "integration: marks tests as integration tests")
    config.addinivalue_line("markers", "e2e: marks tests as end-to-end tests")
    config.addinivalue_line("markers", "ruff: marks tests as ruff checks")
    config.addinivalue_line("markers", "pyright: marks tests as pyright checks")


def pytest_collection_modifyitems(config: Config, items: list[Function]) -> None:
    """Add markers based on test location and reorder tests."""
    static_tests = []
    unit_tests = []
    integration_tests = []
    e2e_tests = []
    other_tests = []

    for item in items:
        # Add markers based on location
        test_path = str(item.fspath)

        if "/static/" in test_path or "\\static\\" in test_path:
            item.add_marker(pytest.mark.static)
            item.add_marker(pytest.mark.check)
            static_tests.append(item)
        elif "/unit/" in test_path or "\\unit\\" in test_path:
            item.add_marker(pytest.mark.unit)
            item.add_marker(pytest.mark.check)
            unit_tests.append(item)
        elif "/integration/" in test_path or "\\integration\\" in test_path:
            item.add_marker(pytest.mark.integration)
            item.add_marker(pytest.mark.check)
            integration_tests.append(item)
        elif "/e2e/" in test_path or "\\e2e\\" in test_path:
            item.add_marker(pytest.mark.e2e)
            e2e_tests.append(item)
        else:
            other_tests.append(item)

        # Add 'all' marker to every test
        item.add_marker(pytest.mark.all)

    # Reorder tests: static → unit → integration → e2e → other
    items[:] = static_tests + unit_tests + integration_tests + e2e_tests + other_tests


def pytest_runtest_setup(item: Function) -> None:
    """Apply timeout based on test type."""
    # Skip if test already has explicit timeout
    if any(marker.name == "timeout" for marker in item.iter_markers()):
        return

    # Detect CI environment
    ci_env = any(
        os.getenv(var)
        for var in ["CI", "GITHUB_ACTIONS", "JENKINS", "TRAVIS", "CIRCLECI"]
    )
    ci_multiplier = float(os.getenv("CI_TIMEOUT_MULTIPLIER", "5.0")) if ci_env else 1.0

    # Apply timeout based on test location
    test_path = str(item.fspath)

    if "/unit/" in test_path or "\\unit\\" in test_path:
        # Unit tests should be fast
        item.add_marker(pytest.mark.timeout(0.1 * ci_multiplier))
    elif "/integration/" in test_path or "\\integration\\" in test_path:
        # Integration tests can take a bit longer
        item.add_marker(pytest.mark.timeout(0.5 * ci_multiplier))
    elif "/e2e/" in test_path or "\\e2e\\" in test_path:
        # E2E tests may take much longer
        item.add_marker(pytest.mark.timeout(30 * ci_multiplier))
    elif "/static/" in test_path or "\\static\\" in test_path:
        # Static analysis can take time
        item.add_marker(pytest.mark.timeout(60 * ci_multiplier))


@pytest.fixture(autouse=True)
def setup_test_environment() -> Iterator[None]:
    """Set up test environment."""
    # Store original env vars
    original_env = os.environ.copy()

    # Disable any telemetry/analytics
    os.environ["{{cookiecutter.project_slug.upper()}}_DISABLE_TELEMETRY"] = "1"

    # Set test environment
    os.environ["{{cookiecutter.project_slug.upper()}}_ENV"] = "test"

    yield

    # Restore original environment
    os.environ.clear()
    os.environ.update(original_env)


@pytest.fixture(autouse=True)
def disable_network(request: pytest.FixtureRequest) -> Iterator[None]:
    """Disable network access for unit tests."""
    # Only disable network for unit tests
    if "unit" in str(request.fspath):
        # For now, just skip network blocking until we fix pytest-socket
        yield
    else:
        yield


@pytest.fixture
def temp_dir(tmp_path: Path) -> Path:
    """Create a temporary directory for tests."""
    return tmp_path


@pytest.fixture
def mock_config() -> Any:
    """Create a mock configuration object."""
    # This will be implemented when we create the configuration system
    from dataclasses import dataclass

    @dataclass
    class MockConfig:
        """Mock configuration for testing."""

        debug: bool = False
        timeout: int = 30

    return MockConfig()
