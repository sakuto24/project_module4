# Generated by Django 4.0.10 on 2023-08-11 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_advertisements', '0003_advertisement_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='image',
            field=models.ImageField(default=1, upload_to='advertisements/', verbose_name='изображение'),
            preserve_default=False,
        ),
    ]
