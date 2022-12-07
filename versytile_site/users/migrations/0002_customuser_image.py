# Generated by Django 4.1.2 on 2022-12-05 20:12

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='image',
            field=models.ImageField(default='default/user.jpg', max_length=255, upload_to=users.models.CustomUser.image_upload_to),
        ),
    ]
