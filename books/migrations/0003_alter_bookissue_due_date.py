# Generated by Django 4.1.6 on 2023-02-16 17:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0002_bookissue"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bookissue",
            name="due_date",
            field=models.DateField(
                default=datetime.datetime(2023, 3, 2, 19, 51, 25, 572851)
            ),
        ),
    ]
