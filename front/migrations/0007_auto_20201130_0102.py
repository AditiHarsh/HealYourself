# Generated by Django 3.1.1 on 2020-11-29 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0006_auto_20201129_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='timing',
            field=models.CharField(max_length=50),
        ),
    ]