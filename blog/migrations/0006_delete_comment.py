# Generated by Django 3.2.5 on 2021-07-23 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20210722_0621'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
