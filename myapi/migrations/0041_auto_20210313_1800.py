# Generated by Django 3.1.7 on 2021-03-13 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0040_auto_20210313_1750'),
    ]

    operations = [
        migrations.CreateModel(
            name='Netflix',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='netflix', max_length=120)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('title', models.CharField(default='', max_length=120)),
                ('description', models.CharField(default='', max_length=5000)),
                ('para1', models.CharField(default='', max_length=200)),
                ('para2', models.CharField(default='', max_length=800)),
                ('para3', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='trending',
            name='now',
            field=models.TimeField(default='18:00:33'),
        ),
    ]
