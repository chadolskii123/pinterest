FROM python:3.8.0

WORKDIR /home/

RUN git clone https://github.com/chadolskii123/pinterest.git

WORKDIR /home/pinterest/

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

RN pip install gunicorn

RUN echo "SECRET_KEY=^wxvla^)#)zfe)svtnwxit%5n55m!978*@^ch95m40t+6dhg0w" > .env

RUN python manage.py migrate

EXPOSE 8000

CMD ["gunicorn", "prep.wsgi", "--bind", "0.0.0.0:8000"]