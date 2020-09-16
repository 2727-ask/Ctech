from django.contrib import admin
from .models import Product
from .models import carauselImgs
from .models import Clients
from .models import contact_us

admin.site.register(Product)
admin.site.register(carauselImgs)
admin.site.register(Clients)
admin.site.register(contact_us)

# Register your models here.