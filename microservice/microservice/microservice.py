from fastapi import FastAPI
from pydantic import BaseModel

import humanize
import datetime as dt

import os

SECRETS_PATH = os.environ.get(
    "SECRETS_PATH", f"{os.path.dirname(os.path.realpath(__file__))}/data/secrets.txt"
)

ROOT_RESPONSE = os.environ.get("ROOT_RESPONSE", "Hello world!")

app = FastAPI()


class Date(BaseModel):
    year: int
    month: int
    day: int
    now: str


@app.get("/")
def root():
    return ROOT_RESPONSE


@app.get("/hello/{name}")
def hello(name: str):
    return f"Hello, {name}!"


@app.get("/ping")
def pong():
    return "pong"


@app.get("/secrets")
def secrets() -> list[str]:
    with open(SECRETS_PATH) as f:
        data = f.readlines()
    return [d.strip() for d in data]


@app.get("/date")
def date() -> Date:
    date = dt.datetime.now()
    response = Date(
        year=date.year,
        month=date.month,
        day=date.day,
        now=humanize.naturaldate(date),
    )
    return response
