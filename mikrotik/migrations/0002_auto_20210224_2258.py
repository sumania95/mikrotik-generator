# Generated by Django 3.1.6 on 2021-02-24 22:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mikrotik', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='number_ticket',
            old_name='number_ticker',
            new_name='number_ticket',
        ),
    ]
