from django.contrib import admin
from .models import Auction, Bid, Category, Comment, User, Watchlist, Categ2

# Register your models here.
admin.site.register(User)
admin.site.register(Auction)
admin.site.register(Watchlist)
admin.site.register(Bid)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Categ2)

