from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Category, Comment, User, Auction, Watchlist, Bid
from .forms import AddAuctionForm, Bid_in_Auction, Comment_in_Auction


def index(request):
    return render(request, "auctions/index.html", {
        "auctions": Auction.objects.all().filter(status='A')
    })

def another(request):
    return render(request, "auctions/another.html", {
        #"auctions": Auction.objects.all().filter(status='A').filter(creator=2)
        "auctions": Auction.objects.filter(creator__username='elisa')
    })

def myauctions(request):
    actualuser=request.user
    print(request.user)
    return render(request, "auctions/myauctions.html", {
        #"auctions": Auction.objects.all().filter(status='A').filter(creator=2)
        "auctions": Auction.objects.filter(creator__username=actualuser.username)
    })

def watchlist(request):
    actualuser=request.user
    print(request.user)
    return render(request, "auctions/watchlist.html", {
        "auctions": Auction.objects.filter(watchlist__user=actualuser)
    })

def categories(request):
    print("Entro al categories en el view")
    return render(request, "auctions/categories.html", {
        "categories": Category.objects.all()
    })

def category(request, category_id):
    print("Category id:",category_id)
    print(Auction.objects.filter(category__id=category_id).count())
    print("Salió de la category en view y va a category.html")
    return render(request, "auctions/category.html", {
        "auctions": Auction.objects.filter(category__id=category_id)
        #"cat": Category.objects.get(id=category_id)
    })

def auction(request, auction_id):
    print("--->auction")
    global user
    winnerisonline=False
    sameuser=False
    actualuser=request.user
    auction=Auction.objects.get(pk=auction_id)
    if auction.creator==actualuser:
        sameuser=True
        print("SON IGUALES")
    else:
        print("NO SON IGUALES")

    if auction.win==actualuser:
        winnerisonline=True
    else:    
        winnerisonline=False

    watchlist=Watchlist.objects.filter(auction__pk=auction_id).filter(user__pk=actualuser.id)
    if watchlist.exists():
        print("Entry contained in queryset")
        print(watchlist)
        watch=True
    else: 
        watch=False

    bids=Bid.objects.filter(auction__pk=auction_id).order_by('-amount')
    print("Records in Bids: ",bids.count())

    comments=Comment.objects.filter(auction__pk=auction_id).order_by('DaT_started')
    print("Records in Comments: ",comments.count())
    
    return render(request, "auctions/auction.html", {
        "auction": auction,
        "watchlist": watch,
        "bids": bids,
        "comments": comments,
        "winnerisonline": winnerisonline,
        "sameuser": sameuser
    })

def comments():
    print("view comments")


def auction2(request, auction_id, slug):
    print("--->auction2")
    global user
    sameuser=False
    actualuser=request.user
    auction=Auction.objects.get(pk=auction_id)    
    print(slug)
    if slug=="follow":        
        ins=Watchlist(user=actualuser,auction=auction)
        ins.save()
        print("The data as been written")

    if slug=="unfollow":
        watchlist=Watchlist.objects.filter(auction__pk=auction_id).filter(user__pk=actualuser.id)
        if watchlist.exists():
            Watchlist.objects.filter(auction__pk=auction_id).filter(user__pk=actualuser.id).delete()
            print("UNFOLLOWING...")

    if slug=="comment":
        comments=Comment.objects.filter(auction__pk=auction_id)
        form = Comment_in_Auction(request.POST)
        if request.method == 'POST':                        
            if form.is_valid():                            
                cd = form.cleaned_data
                mycomment=cd['mycomment']
                print(actualuser.username)
                ins=Comment(auction=auction, user=actualuser, desc=mycomment)
                ins.save()
                #Auction.objects.filter(pk=auction.id).update(currentprice=mybid)
                print("The data as been written")
                return HttpResponseRedirect(reverse('auction', args=[auction_id]))
        else:        
            return render(request, "auctions/comment.html", {
                "form": form,
                "auction": auction,
                "comments": comments
            })        

    if slug=="close":
        bid_1=Bid.objects.filter(auction__pk=auction_id).order_by('-amount')[:1].get()
        #print("To Close - Records: ",bid_1.count())
        print(bid_1.user)
        print(bid_1.auction)
        print(bid_1.amount)
        Auction.objects.filter(pk=auction.id).update(status="I", win=bid_1.user)

    if slug!="bid":
        print("slug!=bid")
        if auction.creator==actualuser:
            sameuser=True
            print("SAME")
        else:
            print("NOT THE SAME")
    
        watchlist=Watchlist.objects.filter(auction__pk=auction_id).filter(user__pk=actualuser.id)
        if watchlist.exists():
            print("Entry contained in queryset:",watchlist)
            watch=True
        else: 
            watch=False

        return render(request, "auctions/auction.html", {
            "auction": auction,
            "watchlist": watch,
            "sameuser": sameuser
        })
    else:
        print("slug==bid")      
        bids=Bid.objects.filter(auction__pk=auction_id)
        print("Records: ",bids.count())  
        if request.method == 'POST':            
            form = Bid_in_Auction(request.POST)
            if form.is_valid():                            
                cd = form.cleaned_data
                mybid=cd['mybid']
                if bids.count() == 0: # if there are not bids...
                    if mybid>=auction.currentprice: # mybid has to be >= than the current price
                        print(actualuser.username)
                        ins=Bid(auction=auction, user=actualuser, amount=mybid)
                        ins.save()
                        Auction.objects.filter(pk=auction.id).update(currentprice=mybid)
                        print("The data as been written")
                        return HttpResponseRedirect(reverse('auction', args=[auction_id]))
                    else:
                        return render(request, 'auctions/auction_bid.html',{'form': form, 'price': auction.currentprice, 'txt': "Your bid cannot be lower than the actual price..." })
                else:       # if there are bids...
                    if mybid>auction.currentprice: # mybid has to be > than the current price
                        print(actualuser.username)
                        ins=Bid(auction=auction, user=actualuser, amount=mybid)
                        ins.save()
                        Auction.objects.filter(pk=auction.id).update(currentprice=mybid)
                        print("The data as been written")
                        return HttpResponseRedirect(reverse('auction', args=[auction_id]))                        
                    else:
                        return render(request, 'auctions/auction_bid.html',{'form': form, 'price': auction.currentprice, 'txt': "Your bid cannot be lower than the actual price..." })    
        else:
            print("TRATO DE IR AL FORM")
            form = Bid_in_Auction(request.POST)
            if bids.count() == 0:
                msg="0 Bids"
            elif bids.count() == 1:
                msg="1 Bid"
            else:
                msg=str(bids.count())+" Bids"    
        return render(request, 'auctions/auction_bid.html',{'form': form, 'price': auction.currentprice ,'txt': msg })

def auction_bid(request, myauction_id):
    print("--->auction_bid")
    global user
    actualuser=request.user
    submitted = False
    if request.method == 'POST':
        form = Bid_in_Auction(request.POST)
        if form.is_valid():            
            cd = form.cleaned_data
            mybid=cd['mybid']
            print(actualuser.username)
            ins=Bid(auction=myauction_id, user=actualuser, amount=mybid)
            ins.save()
            print("The data as been written")
            #return HttpResponseRedirect('auction')
            return render(request, "auctions/auction.html", {
                "auction": myauction_id
            })
    else:
        form = Bid_in_Auction(request.POST)
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'auction_bid',{'form': form})
    #return render(request, 'auction_bid',{'form': form, 'submitted': submitted})

def addauction(request):
    global user
    actualuser=request.user
    submitted = False
    if request.method == 'POST':
        form = AddAuctionForm(request.POST)
        if form.is_valid():            
            cd = form.cleaned_data
            #title=request.POST['title']
            title=cd['title']
            descrip=cd['descrip']
            startingbid=cd['startingbid']
            currentprice=cd['startingbid']
            category=cd['category']
            URLimage=cd['URLimage']
            print(actualuser.username)
            ins=Auction(title=title,descrip=descrip,startingbid=startingbid,currentprice=currentprice,status='A',
                        category_id=category, creator=actualuser, URLimage=URLimage)
            ins.save()
            print("The data as been written")
            # assert False
            #return HttpResponseRedirect('auctions/addauction?submitted=True')
            #return HttpResponseRedirect('addauction?submitted=True')
            return HttpResponseRedirect('addauction')
    else:
        form = AddAuctionForm(request.POST)
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'auctions/addauction.html',{'form': form, 'submitted': submitted})            


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
