# Generated by Django 3.1 on 2020-09-06 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tourit', '0004_itinerary_placetypes'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Places',
            new_name='Place',
        ),
    ]
