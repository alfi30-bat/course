# Generated by Django 5.1.2 on 2024-10-22 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instructor',
            name='course',
        ),
        migrations.AddField(
            model_name='course',
            name='overview',
            field=models.TextField(default='none'),
        ),
    ]
