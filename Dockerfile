FROM python:3.11



ENV PYTHONDJNTWPITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


WORKDIR /app


COPY requarements.txt /app/

RUN pip install -r requarements.txt

COPY . /app/

CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]