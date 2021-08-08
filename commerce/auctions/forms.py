#from auctions.models import Categ2
from django.forms import forms
from django import forms
#from auctions.models import Auction

class AddAuctionForm(forms.Form):
    CATEGORY_CHOICES =(
    ("010000000000000", "Books"),
    ("020000000000000", "Films, Tv, Music & Games"),
    ("030000000000000", "Electronics & Computers"),
    ("040000000000000", "Home, Garden, Home Improvements and Pets"),
    ("050000000000000", "Toys, Children & Baby"),)
    title=forms.CharField(max_length=50, label='Title')
    descrip=forms.CharField(max_length=255, label='Description',widget=forms.Textarea)
    startingbid=forms.DecimalField(max_digits=10, decimal_places=2, label='Starting Bid')
    #currentprice=forms.DecimalField(max_digits=10, decimal_places=2, label='Current Price')
    category=forms.ChoiceField(label='Category', choices=CATEGORY_CHOICES)
    #categ2=forms.CharField(max_length=15, label='Categ2')
    URLimage=forms.URLField(max_length=200, label='Link to image')

class Auc_SameUser_Form(forms.Form):
    title=forms.CharField(max_length=50, label='Title')

class Bid_in_Auction(forms.Form):
    mybid=forms.DecimalField(max_digits=10, decimal_places=2, label='My Bid: ')
    
class Comment_in_Auction(forms.Form):
    mycomment=forms.CharField(max_length=255, label='Comment',widget=forms.Textarea)
    

