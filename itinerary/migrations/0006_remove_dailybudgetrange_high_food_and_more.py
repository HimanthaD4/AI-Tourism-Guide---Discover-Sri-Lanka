# Generated by Django 5.1 on 2024-11-12 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('itinerary', '0005_alter_dailybudgetrange_high_food_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dailybudgetrange',
            name='high_food',
        ),
        migrations.RemoveField(
            model_name='dailybudgetrange',
            name='low_food',
        ),
        migrations.RemoveField(
            model_name='dailybudgetrange',
            name='medium_food',
        ),
    ]
