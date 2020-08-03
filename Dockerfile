FROM python:3.8-buster

RUN apt update
RUN pip install poetry

WORKDIR /app
COPY poetry.lock pyproject.toml /app/

RUN poetry config virtualenvs.create false \
    &&poetry install --no-dev

COPY . /app
CMD python main.py
