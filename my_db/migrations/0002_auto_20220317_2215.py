# Generated by Django 3.2 on 2022-03-17 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_db', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='pers_photo',
        ),
        migrations.AddField(
            model_name='person',
            name='mainPhoto',
            field=models.ImageField(default='work/Without photo.jpg', upload_to='img/', verbose_name='Главное фото'),
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
    ]