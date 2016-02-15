from django.contrib import admin
from .models import Product,ProductImage
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
	date_hierarchy='timestamp'
	search_fields=['title','description']
	list_display=['title','price','active','update',]
	list_editable=['price','active']
	list_filter=['price','active']
	readonly_fields=['timestamp','update']
	prepopulated_fields={'slug':('title',)}

	class Meta:
		model = Product

	class Media:
		js = (
			'/static/js/kindeditor-min.js',
            '/static/js/zh_CN.js',
            '/static/js/config.js',
        )



admin.site.register(Product, ProductAdmin)


admin.site.register(ProductImage)