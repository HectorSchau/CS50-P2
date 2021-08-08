from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("another", views.another, name="another"),
    path("myauctions", views.myauctions, name="myauctions"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("<int:auction_id>", views.auction, name="auction"),
    path("<int:auction_id>/<slug:slug>", views.auction2, name="auction2"),
    path("<int:auction_bid>",views.auction_bid, name="auction_bid"),
    path("addauction",views.addauction, name="addauction"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("comments", views.comments, name="comments"),
    path("categories", views.categories, name="categories"),
    path("specifics/<slug:category_id>", views.category, name="category"),
    path("register", views.register, name="register")
]
