# Generated by Django 2.1.5 on 2019-02-07 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='work_photo',
            field=models.ImageField(default=False, upload_to='media'),
        ),
    ]
