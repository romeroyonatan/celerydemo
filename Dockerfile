FROM python:3.6

RUN mkdir /opt/demo

WORKDIR /opt/demo

ADD requirements.txt .
RUN pip install -r requirements.txt

ADD celerydemo .

EXPOSE 8000

USER 42

CMD python manage.py runserver 0.0.0.0:8000