# Generated by Django 3.2 on 2021-05-23 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_auto_20210523_1047'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('desc', models.CharField(max_length=255)),
            ],
        ),
    ]