# Generated by Django 3.1.1 on 2020-09-30 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20200930_1706'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vendor',
            old_name='vendor',
            new_name='vendor_posting_group',
        ),
    ]
