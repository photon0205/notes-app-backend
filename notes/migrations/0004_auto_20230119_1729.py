# Generated by Django 3.2.16 on 2023-01-19 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_auto_20230111_1340'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='primary',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='note',
            name='secondary',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
