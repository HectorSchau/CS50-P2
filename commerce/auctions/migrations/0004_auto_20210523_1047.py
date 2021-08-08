# Generated by Django 3.2 on 2021-05-23 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auto_20210523_1034'),
    ]

    operations = [
        migrations.DeleteModel(
            name='statusenum',
        ),
        migrations.AddField(
            model_name='auction',
            name='status',
            field=models.CharField(choices=[('A', 'Active'), ('I', 'Inactive')], default='A', max_length=1),
        ),
    ]