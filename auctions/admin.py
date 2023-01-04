from django.contrib import admin

from .models import User, category, listing, bids

# Register your models here.
admin.site.register(User)
admin.site.register(category)
admin.site.register(listing)
admin.site.register(bids)
