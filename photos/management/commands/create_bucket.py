"""
Command to create the initial bucket for storing photos.

Make sure to have the following set in the django settings file:

* AWS_ACCESS_KEY_ID
* AWS_SECRET_ACCESS_KEY
* AWS_STORAGE_BUCKET_NAME
* AWS_S3_HOST

"""

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

import boto
import boto.s3.connection

class Command(BaseCommand):
    help = 'Creates the bucket in S3 for storing static and media files.'

    def handle(self, *args, **options):

        conn = boto.connect_s3(
            aws_access_key_id = settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key = settings.AWS_SECRET_ACCESS_KEY,
            host = settings.AWS_S3_HOST,
            calling_format = settings.AWS_S3_CALLING_FORMAT,
        )

        bucket = conn.create_bucket(settings.AWS_STORAGE_BUCKET_NAME)
        bucket.set_acl('public-read')
