# Generated by Django 3.0.5 on 2020-06-09 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VRCpubs', '0002_vrcpubs_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vrcpubs',
            name='publishedAt',
            field=models.DateTimeField(),
        ),
    ]
