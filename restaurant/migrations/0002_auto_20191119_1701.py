# Generated by Django 2.2.6 on 2019-11-19 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='addr',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
