from .models import Product
from django.shortcuts import render
from django.views.generic import TemplateView
from .filters import ProductsFilter
# # Create your views here.
# def home_view(request):
#     return render(request,'home.html')

class HomeView(TemplateView):
    template_name = 'home.html'
    def get_context_data(self):
        context = super(HomeView, self).get_context_data()
        filters = Product.objects.all()
        product_filter = ProductsFilter(self.request.GET , queryset=filters)
        context['product_filter'] = product_filter
        return context