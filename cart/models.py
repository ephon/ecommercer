from django.db import models
from products.models import Product
from accounts.models import MyUser

class CartItem(models.Model):
	product = models.ForeignKey(Product)
	quantity = models.IntegerField(default=1)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return str(self.id)

# Create your models here.
class Cart(models.Model):
	user = models.OneToOneField(MyUser, null=True, blank=True)
	items = models.ManyToManyField(CartItem, null=True, blank=True)
	total = models.DecimalField(max_digits=50, decimal_places=2, default=0.00)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	update = models.DateTimeField(auto_now=True, auto_now_add=False)
	active = models.BooleanField(default=True)

	def __str__(self):
		return 'Cart id: %s' %self.id

