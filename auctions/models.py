from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class category(models.Model):
    categoryName = models.CharField(max_length=64)

    def __str__(self):
        return self.categoryName

class listing(models.Model):
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=128)
    image = models.CharField(max_length=512)
    price = models.FloatField()
    isActive = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="user")
    category = models.ForeignKey(category, on_delete=models.CASCADE, blank=True, null=True, related_name="cat")
    watchList = models.ForeignKey(User,on_delete=models.CASCADE, blank=True, null=True, related_name="watch")

    def __str__(self):
        return self.title

class bids(models.Model):
    product_title = models.ForeignKey(listing, on_delete=models.CASCADE, blank=True, null=True, related_name="bid")
    bid_price = models.FloatField(blank=True,null=True)
    bidder = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="bidder")
    seller = models.ForeignKey(User,on_delete=models.CASCADE, blank=True, null=True, related_name="seller")

    def __str__(self):
        return self.product_title

class commments(models.Model):
    content = models.CharField(max_length=256)
    product = models.ForeignKey(listing, on_delete=models.CASCADE, blank=True, null=True, related_name="product")
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="commentator")

