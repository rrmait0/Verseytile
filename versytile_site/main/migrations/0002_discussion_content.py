# Generated by Django 4.1.2 on 2022-11-28 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='discussion',
            name='content',
            field=models.TextField(blank=True, default=''),
        ),
    ]
