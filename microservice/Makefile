DOCKER_REGISTRY ?= rafalskolasinski

install:
	poetry install

run-dev:
	poetry run uvicorn microservice:app --port 8080 --reload

fmt:
	poetry run ruff format

lint:
	poetry run ruff check

test:
	poetry run pytest -v .

build:
	docker build -t microservice:latest .

run:
	docker run --rm -it -p 8080:8080 microservice:latest

push:
	docker tag microservice:latest ${DOCKER_REGISTRY}/microservice:python
	docker push ${DOCKER_REGISTRY}/microservice:python
