# Generated by Django 2.2.6 on 2019-10-29 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('letitbeeasy', '0002_content_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='image',
        ),
    ]