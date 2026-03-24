install:
	uv sync

lint:
	uv run ruff check

build:
	./build.sh

render-start:
	gunicorn task_manager.wsgi

run:
	uv run python manage.py runserver

collectstatic:
	uv run python manage.py collectstatic --no-input

migrate:
	uv run python manage.py migrate

test:
	uv run manage.py test
