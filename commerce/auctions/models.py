from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime


class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    def __str__(self):        
        return f"{self.id}: {self.username}"            

class Category(models.Model):
    id=models.CharField(max_length=15, primary_key=True)
    desc=models.CharField(max_length=255)
    def __str__(self):        
        return f"Category {self.id}: {self.desc}"  

class Categ2(models.Model):
    BOOKS='010000000000000'
    FILMS='020000000000000'
    ELECT='030000000000000'
    HOMEG='040000000000000'
    TOYS ='050000000000000'
    CATEGORY_CHOICES=[(BOOKS, 'Books'),
                      (FILMS, 'Films, Tv, Music & Games'),
                      (ELECT, 'Electronics & Computers'),
                      (HOMEG, 'Home, Garden, Home Improvements and Pets'),
                      (TOYS,  'Toys, Children & Baby'),                    ]
    id=models.CharField(max_length=15, primary_key=True)
    categ2=models.CharField(max_length=15,choices=CATEGORY_CHOICES, default=BOOKS)

class Auction(models.Model):
    ACTIVE='A'
    INACTIVE='I'
    STATUS_CHOICES=[(ACTIVE, 'Active'),(INACTIVE, 'Inactive'),]

    id = models.AutoField(primary_key=True)
    title=models.CharField(max_length=50)
    descrip=models.CharField(max_length=255)
    startingbid=models.DecimalField(max_digits=10, decimal_places=2)
    currentprice=models.DecimalField(max_digits=10, decimal_places=2)
    status=models.CharField(max_length=1, choices=STATUS_CHOICES, default=ACTIVE,) 
    DaT_started=models.DateTimeField(auto_now=True)
    URLimage=models.URLField(max_length=200, blank=True)
    pic=models.ImageField(blank=True)
    creator=models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    category=models.ForeignKey(Category, on_delete=models.CASCADE, )
    win=models.ForeignKey(User, related_name='winner', on_delete=models.CASCADE, default=1)
    #categ2=models.ForeignKey(Categ2, on_delete=models.CASCADE, blank=True, default='010000000000000')
    
    def __str__(self):
        return f"{self.category} - {self.id}: {self.title} - Status: {self.status} by: {self.creator}"

class Watchlist(models.Model):
    id = models.AutoField(primary_key=True, )
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1 )
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, )
    def __str__(self):        
        return f"user = {self.user} and auction = {self.auction}"

class Bid(models.Model):
    id = models.AutoField(primary_key=True, )
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE,)
    user = models.ForeignKey(User, on_delete=models.CASCADE, )
    amount=models.DecimalField(max_digits=10, decimal_places=2)
    DaT_started=models.DateTimeField(auto_now=True)

    #def __str__(self):        
    #    return f"Auction: {self.auction} - User: {self.user} - Amount: {self.amount} - (started:{self.DaT_started})"

class Comment(models.Model):
    id = models.AutoField(primary_key=True, )    
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1 )
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, )
    desc = models.CharField(max_length=255)
    DaT_started=models.DateTimeField(auto_now=True)
    def __str__(self):        
        return f"user_id = {self.user} and auc_id = {self.auction}, comment: {self.desc}" 

