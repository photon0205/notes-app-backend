# Generated by Django 3.2.16 on 2023-01-11 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.TextField(primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
    ]
