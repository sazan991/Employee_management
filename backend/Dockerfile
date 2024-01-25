FROM python:3.8

WORKDIR /app
COPY . /app

RUN pip install -r backend/requirements.txt

CMD [ "python", "backend/manage.py", "runserver", "0.0.0.0:8000" ]