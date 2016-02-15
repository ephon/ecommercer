from django.db import models
from accounts.models import MyUser
from cart.models import Cart
# Create your models here.


STATUS_CHOICE = (
                    ("Started", "开始"), ("Abandoned", "删除"), ("Finish", "完成")
                )


class Order(models.Model):
    user = models.ForeignKey(MyUser, blank=True, null=True)
    cart = models.ForeignKey(Cart)
    order_id = models.CharField(max_length=120, default="00000", unique=True)
    sub_total = models.DecimalField(default=00.00, max_digits=120, decimal_places=2 )
    status = models.CharField(max_length=30, choices=STATUS_CHOICE, default="开始")
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)


    def __str__(self):
        return self.order_id






