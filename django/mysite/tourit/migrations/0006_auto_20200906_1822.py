# Generated by Django 3.1 on 2020-09-06 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourit', '0005_auto_20200906_1813'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itinerary',
            name='placetypes',
        ),
        migrations.AddField(
            model_name='place',
            name='placetypes',
            field=models.ManyToManyField(to='tourit.PlaceType'),
        ),
    ]
