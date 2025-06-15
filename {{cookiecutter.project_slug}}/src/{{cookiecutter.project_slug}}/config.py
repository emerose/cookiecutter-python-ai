"""Configuration management for the {{cookiecutter.project_slug}} application.

This module provides immutable configuration objects that separate static
configuration from runtime options.
"""

import os
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class {{cookiecutter.project_class_name}}Config:
    """Immutable configuration for the {{cookiecutter.project_slug}} application.

    Contains static configuration that doesn't change during execution.
    """

    # Application settings
    app_name: str = "{{cookiecutter.project_slug}}"
    version: str = "{{cookiecutter.version}}"
    debug: bool = False

    @classmethod
    def from_env(cls) -> "{{cookiecutter.project_class_name}}Config":
        """Create configuration from environment variables.

        Environment variables:
        - {{cookiecutter.project_slug.upper()}}_DEBUG: Set to "true" to enable debug mode
        """
        return cls(
            debug=os.getenv("{{cookiecutter.project_slug.upper()}}_DEBUG", "false").lower() == "true",
        )

    def with_overrides(self, **kwargs: Any) -> "{{cookiecutter.project_class_name}}Config":
        """Create a new config with overridden values.

        Since the config is immutable, this creates a new instance
        with the specified values changed.
        """
        # Get current values as dict
        current_values = {
            field.name: getattr(self, field.name)
            for field in self.__dataclass_fields__.values()
        }

        # Override with new values
        current_values.update(kwargs)

        return self.__class__(**current_values)


@dataclass
class RuntimeOptions:
    """Mutable runtime options that control application behavior.

    These are flags and callbacks that can change during execution.
    """

    # Output and feedback options
    verbose: bool = False
    quiet: bool = False

    # Runtime flags
    dry_run: bool = False


def load_config() -> {{cookiecutter.project_class_name}}Config:
    """Load configuration from environment with fallbacks.

    This is the main entry point for getting application configuration.
    """
    return {{cookiecutter.project_class_name}}Config.from_env()


def create_runtime_options(
    verbose: bool = False,
    quiet: bool = False,
    dry_run: bool = False,
) -> RuntimeOptions:
    """Create runtime options with common defaults."""
    return RuntimeOptions(
        verbose=verbose,
        quiet=quiet,
        dry_run=dry_run,
    )
