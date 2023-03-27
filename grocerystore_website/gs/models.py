from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    USERNAME_FIELD = 'email'
    email = models.EmailField('User Email')

class RegisteredUser(models.Model):
    USERNAME_FIELD = 'username'
    username = models.CharField('Username', max_length=120)
    email = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    password = models.CharField('Password', max_length=120)
    name = models.CharField('Name', max_length=120)
    address = models.CharField('Address', max_length=120)

class Product(models.Model):
    product_name = models.CharField('Product Name', max_length=120)
    stock = models.IntegerField('Product Stock')
    
class Groceries(models.Model):
    item_id = models.IntegerField('Item ID')
    item_name = models.ForeignKey(Product, blank=True, null=True, on_delete=models.CASCADE)
    item_img = models.FileField('Item Image')
    category = models.CharField('Category', max_length=120)
    stock = models.IntegerField('Stock')
    price = models.FloatField('Price')
    
class Admin(models.Model):
    admin_id = models.IntegerField('AdminID')
    user = models.ForeignKey(RegisteredUser, blank=True, null=True, on_delete=models.CASCADE)


class Orders(models.Model):
    order_id = models.IntegerField('Order ID')
    email = models.EmailField('Order Email')
    address = models.CharField('Address', max_length=120)

class Receipt(models.Model):
    order = models.ForeignKey(Orders, blank=True, null=True, on_delete=models.CASCADE)
    total = models.FloatField('Receipt Total')
    
class Cart(models.Model):
    contents = models.ManyToManyField(Groceries, blank=True)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

class Farm(models.Model):
    farm_name = models.CharField('Farm Name', max_length=120)
    location = models.CharField('Farm Location', max_length=120)

class Suppliers(models.Model):
    supplier_name = models.CharField('Supplier Name', max_length=120)
    product = models.ForeignKey(Product, blank=True, null=True, on_delete=models.CASCADE)
    farm = models.ForeignKey(Farm, blank=True, null=True, on_delete=models.CASCADE)

class Employees(models.Model):
    employee_id = models.IntegerField('Employee ID')
    first_name = models.CharField('First Name', max_length=120)
    last_name = models.CharField('Last Name', max_length=120)
    employer = models.ForeignKey(Suppliers, blank=True, null=True, on_delete=models.CASCADE)
    

