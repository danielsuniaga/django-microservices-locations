FROM python:3.8

WORKDIR /code

RUN pip install poetry

RUN poetry config virtualenvs.create false

COPY pyproject.toml /code/

RUN poetry install

COPY . /code/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
