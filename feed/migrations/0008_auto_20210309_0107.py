# Generated by Django 3.1.6 on 2021-03-09 06:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0007_auto_20210309_0016'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='userComment',
            new_name='comment',
        ),
    ]