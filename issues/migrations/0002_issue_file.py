# Generated by Django 3.0.7 on 2020-08-12 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='file',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
