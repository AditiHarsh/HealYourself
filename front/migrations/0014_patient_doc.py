# Generated by Django 3.1.1 on 2020-11-30 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0013_remove_patient_doc_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='doc',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
