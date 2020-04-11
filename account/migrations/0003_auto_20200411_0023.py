# Generated by Django 2.1 on 2020-04-10 18:53

import account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20200410_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.FileField(default='profile_img/user.png', null=True, upload_to=account.models.get_image_name),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='image',
            field=models.FileField(default='profile_img/user.png', null=True, upload_to=account.models.get_image_name1),
        ),
    ]
