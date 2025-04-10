.PHONY: clean clean-test clean-pyc clean-build docs help setup dev test lint format pre-commit
.DEFAULT_GOAL := help

define BROWSER_PYSCRIPT
import os, webbrowser, sys

from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

BROWSER := python -c "$$BROWSER_PYSCRIPT"

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

setup: ## setup development environment
	pip install -e ".[dev]"
	pre-commit install

dev: ## install development dependencies
	pip install -e ".[dev]"

lint: ## check style with ruff, black, isort, and mypy
	ruff .
	black --check .
	isort --check .
	mypy .

format: ## format code with black and isort
	black .
	isort .

test: ## run tests quickly with pytest
	pytest

test-coverage: clean-test ## run tests with coverage report
	pytest --cov=aether --cov-report=html
	$(BROWSER) htmlcov/index.html

pre-commit: ## run pre-commit on all files
	pre-commit run --all-files

docs: ## generate documentation
	sphinx-build -b html docs docs/_build/html
	$(BROWSER) docs/_build/html/index.html

install: clean ## install the package to the active Python's site-packages
	pip install .

dist: clean ## builds source and wheel package
	python -m build
	ls -l dist

release: dist ## package and upload a release
	twine upload dist/*

init-project: ## initialize project structure
	mkdir -p aether/{core,tokenizers,parsers,models,metrics,visualization,cli,utils}
	mkdir -p tests/{core,tokenizers,parsers,models,metrics,visualization,cli,utils}
	mkdir -p docs/{api,examples,guides}
	touch aether/__init__.py
	touch aether/{core,tokenizers,parsers,models,metrics,visualization,cli,utils}/__init__.py
	touch tests/__init__.py
	touch tests/{core,tokenizers,parsers,models,metrics,visualization,cli,utils}/__init__.py
