# Generated by Django 3.2 on 2021-06-21 22:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_remove_auction_categ2'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='win',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='winner', to=settings.AUTH_USER_MODEL),
        ),
    ]
