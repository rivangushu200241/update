# Generated by Django 3.0.7 on 2020-06-09 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VRCpubs', '0003_auto_20200608_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vrcpubs',
            name='isbn',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
