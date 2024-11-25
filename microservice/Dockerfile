FROM python:3.12

# Prepare working directories
ENV POETRY_HOME /opt/poetry
ENV WORKDIR /microservice
ENV PATH "$POETRY_HOME/bin:$PATH"

WORKDIR $WORKDIR

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
RUN poetry config virtualenvs.create false

# Install environment (just deps so code change does not affect docker caching)
COPY poetry.lock pyproject.toml ${WORKDIR}/
RUN poetry install && rm ~/.cache/pip -rf

# Install microservice
COPY microservice/ /microservice/
RUN poetry install

# Run Microservice
CMD poetry run uvicorn microservice:app --host 0.0.0.0 --port 8080
