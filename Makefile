install:
	poetry inslall

brain-games:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-force-reinstall:
	python3 -m pip install --force-reinstall dist/*.whl

lint:
	poetry run flake8 brain_games
