# {{cookiecutter.project_name}}

A Python application built with modern tooling.

## Requirements

- Python 3.12+
- [uv](https://github.com/astral-sh/uv) for dependency management

## Setup

1. Install uv if you haven't already:
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd {{cookiecutter.project_slug}}
   ```

3. Install dependencies:
   ```bash
   uv sync --dev
   ```

## Development

### Running the application
```bash
uv run python -m {{cookiecutter.project_slug}}
```

### Running tests
```bash
uv run pytest
```

### Linting and formatting
```bash
# Check code style
uv run ruff check .

# Format code
uv run ruff format .
```

### Type checking
```bash
uv run pyright
```

## Project Structure

```
{{cookiecutter.project_slug}}/
├── src/{{cookiecutter.project_slug}}/          # Application source code
├── tests/              # Test files
├── .github/            # GitHub Actions workflows
├── pyproject.toml      # Project configuration
├── .cursorrules        # Cursor IDE configuration
└── CLAUDE.md          # Claude AI assistant instructions
```

## Contributing

1. Create a feature branch
2. Make your changes
3. Ensure all tests pass and code is properly formatted
4. Submit a pull request

All pull requests will run through CI checks including:
- Tests on Python 3.12
- Linting with ruff
- Type checking with pyright