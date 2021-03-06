FROM python:3.8.0

WORKDIR /home/

RUN git clone https://github.com/chadolskii123/pinterest.git

WORKDIR /home/pinterest/

RUN echo "asdfa"

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

RUN echo "SECRET_KEY=^wxvla^)#)zfe)svtnwxit%5n55m!978*@^ch95m40t+6dhg0w" > .env

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["bash", "-c", "python manage.py migrate --settings=prep.settings.deploy && gunicorn prep.wsgi --env DJANGO_SETTINGS_MODULE=prep.settings.deploy --bind 0.0.0.0:8000"]