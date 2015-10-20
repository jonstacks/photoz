# photoz

A Django project for an AWS S3 backed, temporary image store.

If you've ever needed a place to temporarily upload a file and provide a
URL to that file, this project might be for you. This project was inspired
because we had an internal pastebin type solution, but not an internal
temporary image service.

## Installation

### Run migrations

    python manage.py makemigrations
    python manage.py migrate

### Create a super user so you can use the admin

    python manage.py createsuperuser

### Create your cloud bucket.

    python manage.py create_bucket

### Copy static files to the cloud!

The following command will copy your static files to s3 so that they will be
served up from the "cloud" allowing the photoz app to do other things instead.

    python manage.py collectstatic --noinput

## Configuration

If you are running this project locally, and not from a docker container,
you will need to make sure the following environment variables get set:

* AWS_STORAGE_BUCKET_NAME
* AWS_ACCESS_KEY_ID
* AWS_SECRET_ACCESS_KEY

You can also mess around with the [settings.py](photoz/settings.py) file
to change the configuration to your liking.

## Deployment

Deployment with [Docker](https://www.docker.com/) is easy! This project comes
with a [Dockerfile](Dockerfile) so you can easily build and deploy it. All
you need to do is set the following environment variables:

* AWS_STORAGE_BUCKET_NAME
* AWS_ACCESS_KEY_ID
* AWS_SECRET_ACCESS_KEY

Optionally, you can also set the `AWS_S3_HOST` environment variable if you
are storing your data in some place otehr than `s3.amazonaws.com`.

And connect it up to a `postgres` database container. See the
[docker-compose.yml](docker-compose.yml) file for an example.
