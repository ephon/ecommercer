from django.shortcuts import render, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from products.models import Product
from .models import Cart, CartItem
# Create your views here.


def update_total(cart):
	new_total = 0.00
	for item in cart.items.all():
		new_total += float(item.product.price) * item.quantity
	cart.total = new_total
	cart.save()

def view(request):
	if request.user.is_authenticated():
		try:
			cart = Cart.objects.get(user=request.user)
		except:
			message = "你的购物车里还没有什么东西呢！ "
			render(request, 'cart/view.html', locals())
	else:
		message = "请登陆查后再查看你的购物车！ "
	return render(request, 'cart/view.html', locals())

@login_required
def add_to_cart(request, slug):
	if request.user.is_authenticated():
		cart, created = Cart.objects.get_or_create(user=request.user)
	try:
		product = Product.objects.get(slug=slug)
	except Product.DoesNotExist:
		raise Http404
	cart_item, created = CartItem.objects.get_or_create(product=product)
	if not created and cart_item in cart.items.all():
		cart_item.quantity += 1
		cart_item.save()
	else:
		cart.items.add(cart_item)
	update_total(cart)
	return HttpResponseRedirect(reverse('cart'))


def remove_item(request, pid):
	try:
		item = CartItem.objects.get(id=pid)
		cart = Cart.objects.get(user=request.user)
		cart.items.remove(item)
		item.delete()
		cart.save()
		update_total(cart)
		return HttpResponseRedirect(reverse('cart'))
	except:
		raise Http404


def add_qty(request, pid):
	try:
		item = CartItem.objects.get(id=pid)
		item.quantity += 1
		item.save()
		if request.user.is_authenticated():
			cart = Cart.objects.get(user=request.user)
		else:
			cart = Cart.objects.get(id=request.session['cart_id'])
		update_total(cart)
		return HttpResponseRedirect(reverse('cart'))
	except:
		raise Http404


def sub_qty(request, pid):
	try:
		item = CartItem.objects.get(id=pid)
		item.quantity -= 1
		item.save()
		if request.user.is_authenticated():
			cart = Cart.objects.get(user=request.user)
		else:
			cart = Cart.objects.get(id=request.session['cart_id'])
		update_total(cart)
		return HttpResponseRedirect(reverse('cart'))
	except:
		raise Http404
