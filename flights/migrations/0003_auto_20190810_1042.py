# Generated by Django 2.2b1 on 2019-08-10 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0002_passengers'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Passengers',
            new_name='Passenger',
        ),
    ]
