FROM python:3.7.6-stretch
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
RUN apt-get install sqlite3 -y
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

#For deployment
# CMD ["uwsgi", "app.ini"]

#For development
CMD ["python", "run.py"]