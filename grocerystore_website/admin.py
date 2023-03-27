from django.contrib import admin
from .gs import User
from .gs import RegisteredUser
from .gs import Product
from .gs import Groceries
from .gs import Admin
from .gs import Orders
from .gs import Receipt
from .gs import Cart
from .gs import Farm
from .gs import Suppliers
from .gs import Employees


admin.site.register(User)
admin.site.register(RegisteredUser)
admin.site.register(Product)
admin.site.register(Groceries)
admin.site.register(Admin)
admin.site.register(Orders)
admin.site.register(Receipt)
admin.site.register(Cart)
admin.site.register(Farm)
admin.site.register(Suppliers)
admin.site.register(Employees)