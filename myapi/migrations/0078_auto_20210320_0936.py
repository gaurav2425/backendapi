# Generated by Django 3.1.7 on 2021-03-20 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0077_auto_20210320_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amazon',
            name='now',
            field=models.TimeField(default='09:36:38'),
        ),
        migrations.AlterField(
            model_name='hot',
            name='description',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='hot',
            name='name',
            field=models.CharField(default='hot', max_length=120),
        ),
        migrations.AlterField(
            model_name='hot',
            name='now',
            field=models.TimeField(default='09:36:38'),
        ),
        migrations.AlterField(
            model_name='new',
            name='now',
            field=models.TimeField(default='09:36:38'),
        ),
        migrations.AlterField(
            model_name='trending',
            name='now',
            field=models.TimeField(default='09:36:38'),
        ),
    ]
