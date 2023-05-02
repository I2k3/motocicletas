FROM python:3
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /motocicletas
WORKDIR /motocicletas
COPY requirements.txt /motocicletas/
RUN pip install -r requirements.txt
COPY . /motocicletas/
CMD python manage.py runserver --settings=settings.production 0.0.0.0:8080