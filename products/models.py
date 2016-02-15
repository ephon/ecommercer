from django.db import models

# Create your models here.


class Product(models.Model):
	title = models.CharField(max_length=120)
	description = models.TextField(null=True, blank=True)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	sale_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
	slug = models.SlugField(unique=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	update = models.DateTimeField(auto_now_add=False, auto_now=True)
	active = models.BooleanField(default=True)


	def __str__(self):
		return self.title




class ProductImage(models.Model):
	product=models.ForeignKey(Product)
	image = models.ImageField(upload_to='product/images', null=True, blank=True )
	thumbnail=models.BooleanField(default=False)
	featured=models.BooleanField(default=False)
	active=models.BooleanField(default=True)
	updated=models.DateTimeField(auto_now_add=False, auto_now=True)


	def __str__(self):
		return self.product.title
