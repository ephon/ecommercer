"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .upload import upload_image

urlpatterns = patterns('',
    # Examples:
    url(r'^admin/upload/(?P<dir_name>[^/]+)$', upload_image, name='upload_image'),
    url(r'media/(?P<path>.*)$', "django.views.static.serve", {"document_root": settings.MEDIA_ROOT}),
    url(r'^$', 'ecommerce.views.home', name='home'),
    url(r'^s/$', 'ecommerce.views.search', name='search'),
    url(r'^products/$', 'ecommerce.views.home', name='home'),
    url(r'^cart/$', 'cart.views.view', name='cart'),
    url(r'^products/(?P<slug>.*)/$', 'products.views.single', name='single_product'),
    url(r'^cart/(?P<slug>.*)/$', 'cart.views.add_to_cart', name='add_to_cart'),
    url(r'^cart/remove/(?P<pid>\d+)$', 'cart.views.remove_item', name='remove_item'),
    url(r'^cart/add_qty/(?P<pid>.*)$', 'cart.views.add_qty', name='add_qty'),
    url(r'^cart/sub_qty/(?P<pid>.*)$', 'cart.views.sub_qty', name='sub_qty'),
    url(r'^accounts/register', 'accounts.views.register', name='register'),
    url(r'^accounts/login', 'accounts.views.auth_login', name='login'),
    url(r'^accounts/logout', 'accounts.views.auth_logout', name='logout'),
    url(r'^checkout', 'order.views.checkout', name='checkout'),
    url(r'^orders', 'order.views.orders', name='user_orders'),


    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
