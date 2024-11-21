FROM python:3.11.5-slim-bullseye

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

#Install curl
RUN apt update && apt install -y curl

# install gdal GDAL
RUN apt-get update && apt-get install -y gdal-bin libgdal-dev
#Install poetry - package-dep manager
RUN pip install poetry

COPY poetry.lock pyproject.toml /code/

#Install deps
RUN poetry config virtualenvs.create false
RUN poetry install

COPY . /code
