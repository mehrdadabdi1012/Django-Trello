# Generated by Django 4.2.1 on 2024-09-09 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_myuser_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='is_senior',
            field=models.BooleanField(default=False),
        ),
    ]
