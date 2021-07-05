# Generated by Django 3.1.4 on 2021-07-02 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='myuser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default=None, max_length=64)),
                ('email', models.EmailField(default=None, max_length=100, unique=True)),
                ('password', models.CharField(default=None, max_length=64)),
                ('first_name', models.CharField(default=None, max_length=64)),
                ('last_name', models.CharField(default=None, max_length=64)),
            ],
        ),
    ]
