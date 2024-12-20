# Generated by Django 5.1 on 2024-11-14 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itinerary', '0011_alter_location_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='route',
            name='location',
        ),
        migrations.AddField(
            model_name='route',
            name='locations',
            field=models.ManyToManyField(to='itinerary.location'),
        ),
        migrations.AlterField(
            model_name='location',
            name='image_url',
            field=models.URLField(),
        ),
    ]
