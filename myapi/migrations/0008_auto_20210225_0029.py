# Generated by Django 3.1.7 on 2021-02-24 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0007_amazon_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amazon',
            name='description',
            field=models.CharField(default='', max_length=5000),
        ),
    ]
