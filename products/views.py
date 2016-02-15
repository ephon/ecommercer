from django.shortcuts import render_to_response,RequestContext
from .models import Product,ProductImage
# Create your views here.

def single(request, slug):
	product = Product.objects.get(slug=slug)
	images = ProductImage.objects.filter(product=product)

	return render_to_response('products/single.html',  locals(), context_instance=RequestContext(request))





