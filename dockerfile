FROM python:3.11.5
COPY . /app
WORKDIR /app
RUN conda install -r requirements.txt
EXPOSE $PORT
CMD gunicorn --worker=4 --bind 0.0.0.0:$PORT app:app 