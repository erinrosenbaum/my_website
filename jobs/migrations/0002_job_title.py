# Generated by Django 2.1.7 on 2019-02-25 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='title',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
