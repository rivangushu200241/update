# Generated by Django 3.0.5 on 2020-06-09 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VRCpubs', '0003_auto_20200609_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vrcpubs',
            name='publishedAt',
            field=models.DateField(),
        ),
    ]
