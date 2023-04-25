FROM python:3
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /motorcycles
WORKDIR /motorcycles
COPY requirements.txt /motorcycles/
RUN pip install -r requirements.txt
COPY . /motorcycles/
CMD python manage.py runserver --settings=settings.production 0.0.0.0:8080