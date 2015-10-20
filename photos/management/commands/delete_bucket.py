"""
Command to delete the bucket for storing photos and static files.

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
    help = 'Deletes the bucket in S3 for storing static and media files.'

    def add_arguments(self, parser):
        parser.add_argument('-f', '--force',
            action='store_true',
            dest='force',
            default=False,
            help="Will empty the bucket before delting it.")

    def handle(self, **options):
        conn = boto.connect_s3(
            aws_access_key_id = settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key = settings.AWS_SECRET_ACCESS_KEY,
            host = settings.AWS_S3_HOST,
            calling_format = settings.AWS_S3_CALLING_FORMAT,
        )

        bucket = conn.lookup(settings.AWS_STORAGE_BUCKET_NAME)
        if bucket is None:
            raise CommandError('Bucket "%s" does not exist' %
                settings.AWS_STORAGE_BUCKET_NAME)

        keys = bucket.get_all_keys()
        if keys:
            if options['force']:
                # Emtpy the bucket first
                for k in keys:
                    k.delete()
                    self.stdout.write('Deleted key "%s"' % k.name)
            else:
                raise CommandError('Bucket "%s" is not empty' % bucket.name)

        try:
            conn.delete_bucket(bucket)
        except boto.exception.S3ResponseError as e:
            raise CommandError(e.body)
        else:
            self.stdout.write('Deleted bucket "%s"' % bucket.name)
