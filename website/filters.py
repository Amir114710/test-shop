import django_filters
from website.models import Product

class ProductsFilter(django_filters.FilterSet):
    
    class Meta:
        model = Product
        fields = {'categories':['exact'] , 'size':['exact'] ,  'color':['exact'] , 'price':['exact']}
