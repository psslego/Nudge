# Generated by Django 2.2.1 on 2019-05-03 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Food_name', models.CharField(max_length=30)),
                ('ingredient1', models.CharField(max_length=30)),
                ('ingredient2', models.CharField(max_length=30)),
                ('ingredient3', models.CharField(max_length=30)),
            ],
        ),
    ]
