# Generated by Django 3.1.2 on 2020-10-31 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_remove_to_do_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='to_do',
            name='end_day',
        ),
        migrations.RemoveField(
            model_name='to_do',
            name='start_day',
        ),
    ]