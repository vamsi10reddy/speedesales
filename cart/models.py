from django.db import models
from django.conf import settings
from shortuuid.django_fields import ShortUUIDField
from core.models import Product  # You still need a relationship with Product

STATUS_CHOICE = (
    ("process", 'Processing'),
    ("shipped", 'Shipped'),
    ("delivered", 'Delivered'),
)

class CartOrder(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=1.99)
    paid_status = models.BooleanField(default=False)
    order_date = models.DateTimeField(auto_now_add=True)
    product_status = models.CharField(choices=STATUS_CHOICE, max_length=10, default="process")

    class Meta:
        verbose_name_plural = 'Cart Orders'


class CartOrderItems(models.Model):
    order = models.ForeignKey(CartOrder, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=1.99)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=1.99)
    invoice_num = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f"Order {self.order} contains {self.qty} of {self.product}"

    class Meta:
        verbose_name_plural = 'Cart Order Items'
        unique_together = ['order', 'product']        


class Address(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=True)
    status = models.BooleanField(default=False)
