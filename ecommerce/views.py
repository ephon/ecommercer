__author__ = 'p'

from django.shortcuts import render_to_response,RequestContext
from products.models import Product,ProductImage


def home(request):
	products=Product.objects.all()

	return render_to_response('home.html', locals(), context_instance=RequestContext(request))



def search(request):
	try:
		q = request.GET['q']
	except:
		q=None
	if q:
		products = Product.objects.filter(title__icontains=q)


	return render_to_response('products/result.html', locals(), context_instance=RequestContext(request))



def all(request):
	return render_to_response('all')
