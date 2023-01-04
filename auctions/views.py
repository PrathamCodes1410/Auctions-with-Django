from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import User, category, listing, bids


@login_required(login_url='/login') #decorater imported
def listing_display(request):
    if request.method == 'POST':
        title = request.POST["title"]
        item = listing.objects.filter(title=title)
        #bid = bids.objects.filter(product_title=title)
        return render(request, "auctions/display.html", {"product": item})

def watchlist(request):
    user = request.user()
    pass

#def Display_watchlist(request):
#   pass


def index(request):
    display = listing.objects.filter(isActive=True)
    categories = category.objects.all()
    return render(request, "auctions/index.html", {
        "display": display,
        "category" : categories
    })

def filterPage(request):
    if request.method == 'POST':
        cat = request.POST["category"]
        display = listing.objects.filter( category__categoryName__contains=cat )
        categories = category.objects.all()
        return render(request, "auctions/index.html", {
            "display": display,
            "category": categories
        })
        


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


def create_listing(request):
    allCategories = category.objects.all()
    return render(request, "auctions/create_listing.html", {
        "category": allCategories
    })


def save_listing(request):
    if request.method == "POST":
        title = request.POST['title']
        desc = request.POST['Description']
        image_url = request.POST['image']
        price = request.POST['price']
        cat = request.POST['category']
        owner = request.user

    enterCat = category.objects.get(categoryName=cat)

    entry = listing(
        title=title,
        description=desc,
        image=image_url,
        price=float(price),
        category=enterCat,
        owner=owner,
    )

    """entry_bid = bids(
        product_title=title,
        bid_price=float(price),
        seller=owner,
    )
    entry_bid.save()"""
    entry.save()

    return HttpResponseRedirect(reverse(index))
