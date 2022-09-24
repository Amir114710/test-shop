from django.contrib import admin
from .models import Category , Size , Color , Price , Product

admin.site.register(Category)
admin.site.register(Size)
admin.site.register(Color)
admin.site.register(Price)
admin.site.register(Product)
