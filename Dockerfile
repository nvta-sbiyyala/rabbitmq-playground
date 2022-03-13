FROM python:3.9-slim AS build

WORKDIR /app

RUN pip install poetry==1.1.12

COPY . /app/

RUN poetry config virtualenvs.in-project true && poetry install --no-dev -vvv

CMD [ "python", "driver.py" ]
