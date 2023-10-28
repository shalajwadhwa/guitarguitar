from django.db import models
from django.conf import settings


# Create your models here.
def uid_path(instance, filename):
    return "user_{0}/{1}".format(instance.user.id, filename)


class Customer(models.Model):
    customer_id = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    email = models.EmailField(max_length=256)
    phone_number = models.CharField(max_length=30)
    avatar = models.URLField(max_length=200)
    address = models.JSONField()
    loyalty_level = models.IntegerField()

    def __str__(self):
        return "{0}: {1} {2}".format(self.customer_id, self.first_name, self.last_name)


class Orders(models.Model):
    order_id = models.IntegerField(unique=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    shipping_address = models.JSONField()
    products = models.JSONField()
    date_created = models.DateField()
    order_total = models.FloatField()
    order_status = models.IntegerField()

    def __str__(self):
        return "{0}: {1}".format(self.order_id, self.customer_id)


class Products(models.Model):
    sku_id = models.CharField(max_length=15, unique=True)
    asn = models.CharField(max_length=12)
    category = models.CharField(max_length=10)
    online = models.BooleanField()
    item_name = models.CharField(max_length=256)
    brand_name = models.CharField(max_length=256)
    description = models.CharField(max_length=2000, null=True)
    product_detail = models.CharField(max_length=1000, null=True)
    sales_price = models.FloatField()
    picture_main = models.URLField()
    qty_in_stock = models.IntegerField()
    qty_on_order = models.IntegerField()
    colour_option = models.IntegerField()
    pickup_option = models.IntegerField()
    created_on = models.DateField()
    body_shape = models.IntegerField()

    def __str__(self):
        return "(qualities for {0}: category: '{1}', online: '{2}', item name: '{3}', brand name: '{4}', description: '{5}', product detail: '{6}', sales price: '{7}', quantity in stock: '{8}', quantity on order: '{9}', colour options: '{10}', pickup options: '{11}', created on: '{12}', body shape: '{13}') ".format(self.sku_id, self.category, self.online, self.item_name, self.brand_name, self.description, self.product_detail, self.sales_price, self.qty_in_stock, self.qty_on_order, self.colour_option, self.pickup_option, self.created_on, self.body_shape)


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user_customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)
