# Generated by Django 3.2 on 2021-04-27 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auto_20210426_2304'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctions',
            name='auc_currentprice',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='auctions',
            name='auc_datestart',
            field=models.DateTimeField(default=''),
        ),
        migrations.AddField(
            model_name='auctions',
            name='auc_desc',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='auctions',
            name='auc_startbid',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
