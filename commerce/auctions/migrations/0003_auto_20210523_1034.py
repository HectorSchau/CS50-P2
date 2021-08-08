# Generated by Django 3.2 on 2021-05-23 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_auto_20210523_0941'),
    ]

    operations = [
        migrations.CreateModel(
            name='statusenum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('A', 'Active'), ('I', 'Inactive')], default='A', max_length=1)),
            ],
        ),
        migrations.RemoveField(
            model_name='auction',
            name='status',
        ),
    ]