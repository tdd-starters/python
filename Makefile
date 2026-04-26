init:
	uv sync

lint:
	uv run ruff check src tests

stylecheck:
	uv run black --check src/ tests/

format:
	uv run black src/ tests/

typecheck:
	uv run mypy --namespace-packages --explicit-package-bases src/

test:
	uv run pytest --cov --cov-branch --cov-report term-missing

ci: stylecheck lint typecheck test
