from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Auctions(models.Model):
    auc_id=models.CharField(max_length=20)
    auc_title=models.CharField(max_length=50)
    auc_desc=models.TextField
    auc_startbid=models.FloatField
    auc_currentprice=models.FloatField
    auc_status=models.CharField(max_length=1)
    cat_id=models.CharField(max_length=3)



