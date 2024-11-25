# Sample Python Microservice

This is a simple Python microservice written using [FastAPI](https://fastapi.tiangolo.com/).

## Dev Environment

Dev environment is defined using [mise](https://mise.jdx.dev/) and [Poetry](https://python-poetry.org/). This allows to lock versions of all direct and in-direct Python dependencies (Poetry) and version of Python/Poetry themselves (mise).

A [Makefile](./Makefile) target is provided for convenience.

## Distribution

Sample microservice is packaged as Docker image and uploaded to DockerHub as [rafalskolasinski/microservice:python](https://hub.docker.com/r/rafalskolasinski/microservice/tags).
