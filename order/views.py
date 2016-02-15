from django.shortcuts import render,HttpResponseRedirect
import time
from django.core.urlresolvers import reverse
from .models import Order
from cart.models import Cart
# Create your views here.


def orders(request):

    return render(request, 'order/user_orders.html', locals())



def checkout(request):
    try:
        the_id = request.session['cart_id']
        cart = Cart.objects.get(id=the_id)
    except:
        the_id = None
        HttpResponseRedirect(reverse("cart"))

    new_order, created = Order.objects.get_or_create(cart=cart)
    if created:
        new_order.order_id = str(time.time())
        new_order.save()
    new_order.user = request.user
    new_order.save()

    if new_order.status == "完成":
        cart.delete()
        del request.session['cart_id']
        del request.session['items_total']
        return HttpResponseRedirect(reverse("cart"))
    return render(request, 'order/user_orders.html', locals())





