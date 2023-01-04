from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_listing", views.create_listing, name="create_listing"),
    path("save_listing", views.save_listing, name="save_listing"),
    path("listing_display", views.listing_display, name="list"),
    path("filterPage", views.filterPage, name="filterPage"),
    path("watchlist", views.watchlist, name="watchlist"),
    #path("Display_watchlist", views.Display_watchlist, name="Display_watchlist"),
    #path("Add_watchlist", views.Add_watchlist, name="Add_watchlist"),
    #path("Sub_watchlist", views.Sub_watchlist, name="Sub_watchlist"),
]
