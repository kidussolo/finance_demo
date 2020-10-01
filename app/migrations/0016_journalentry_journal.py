# Generated by Django 3.1.1 on 2020-10-01 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_journalentry_journalentryline'),
    ]

    operations = [
        migrations.AddField(
            model_name='journalentry',
            name='journal',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='app.journal'),
            preserve_default=False,
        ),
    ]
