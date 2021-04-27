from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Auctions(models.Model):
    auc_id=models.CharField(max_length=20, primary_key=True)
    auc_title=models.CharField(max_length=50)
    auc_desc=models.CharField(max_length=250, default="")
    auc_startbid=models.DecimalField(max_digits=10, decimal_places=2, default=0)
    auc_currentprice=models.DecimalField(max_digits=10, decimal_places=2, default=0)
    auc_status=models.CharField(max_length=1)
    auc_datestart=models.DateTimeField(default="")
    cat_id=models.CharField(max_length=3)

    def __str__(self):
        return f"{self.auc_id}: {self.auc_title}"




