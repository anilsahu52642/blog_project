# Generated by Django 3.1.4 on 2021-07-02 15:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app1', '0002_auto_20210702_1659'),
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Title', max_length=64)),
                ('content', models.CharField(default=None, max_length=64)),
                ('photo', models.ImageField(upload_to='image')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='myuser',
        ),
    ]