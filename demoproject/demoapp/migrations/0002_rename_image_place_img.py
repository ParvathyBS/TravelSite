# Generated by Django 4.1.1 on 2022-10-06 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='image',
            new_name='img',
        ),
    ]
