# Generated by Django 3.1.1 on 2020-11-30 06:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0010_auto_20201130_1137'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='doctor',
            new_name='doc_name',
        ),
    ]
