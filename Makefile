.PHONY: install
install:
	poetry install

.PHONY: brain-games
brain-games:
	poetry run brain-games

.PHONY: build
build:
	poetry build

.PHONY: publish
publish:
	poetry publish --dry-run

.PHONY: package-install
package-install:
	python3 -m pip install --user --force-reinstall dist/*.whl

.PHONY: lint
lint:
	poetry run flake8 brain_games

.PHONY: brain-even
brain-even:
	poetry run brain-even

.PHONY: brain-calc
brain-calc:
	poetry run brain-calc

.PHONY: brain-gcd
brain-gcd:
	poetry run brain-gcd

.PHONY: brain-progression
brain-progression:
	poetry run brain-progression
