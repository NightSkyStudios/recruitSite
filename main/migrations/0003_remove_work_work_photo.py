# Generated by Django 2.1.5 on 2019-02-07 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_work_work_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='work',
            name='work_photo',
        ),
    ]