FROM python:3.4

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY . /usr/src/app
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80
CMD ["gunicorn", "photoz.wsgi", "-b", "0.0.0.0:80"]
