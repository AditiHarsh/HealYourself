# Generated by Django 3.1.1 on 2020-11-30 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0015_auto_20201130_1155'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='doc',
        ),
        migrations.AddField(
            model_name='patient',
            name='doctor',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
