# Generated by Django 3.1.7 on 2021-05-12 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0002_auto_20210512_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(verbose_name='Created on'),
        ),
    ]
