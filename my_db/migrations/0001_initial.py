# Generated by Django 3.2 on 2021-04-11 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('company_name', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('city', models.CharField(max_length=45)),
                ('phone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=60)),
                ('first_name', models.CharField(max_length=45)),
                ('middle_name', models.CharField(max_length=60)),
                ('mob_phone', models.IntegerField(unique=True)),
                ('sec_phone', models.IntegerField()),
                ('e_mail', models.EmailField(max_length=254, unique=True)),
                ('city', models.CharField(default='Moscow', max_length=45)),
                ('messenger', models.CharField(max_length=45)),
                ('messenger_id', models.CharField(max_length=120)),
                ('comments', models.TextField()),
                ('resume', models.FileField(upload_to='')),
                ('current_company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='my_db.company')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vacancy', models.CharField(max_length=120)),
                ('project_name', models.CharField(max_length=120)),
                ('comments', models.TextField()),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='my_db.company')),
                ('persons', models.ManyToManyField(related_name='long_list_persons', to='my_db.Person')),
            ],
        ),
    ]
