"""
Command to list the bucket contents.

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
from prettytable import PrettyTable


class Command(BaseCommand):
    help = 'List the contents of the static and media files bucket in S3.'

    def bytes_to_kb(self, byts):
        return float(byts)/ 1024

    def handle(self, *args, **options):
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

        table = PrettyTable([
            "Key", "Last Modified", "Size (KB)", "Version ID"
        ])
        table.align["Key"] = "l"
        table.align["Size (KB)"] = "r"
        for key in bucket.list():
            table.add_row([
                key.name,
                key.last_modified,
                self.bytes_to_kb(key.size),
                key.version_id,
            ])

        print table

