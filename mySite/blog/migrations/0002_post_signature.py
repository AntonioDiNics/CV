# Generated by Django 4.2.2 on 2023-06-26 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='signature',
            field=models.CharField(default='Antonio', max_length=140),
        ),
    ]
