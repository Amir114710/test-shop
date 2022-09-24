from django.db import models
from colorfield.fields import ColorField
class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'دسته بندی ها'
        verbose_name = 'دسته بندی'
class Size(models.Model):
    number = models.CharField(max_length=100)

    def __str__(self):
        return self.number

    class Meta:
        verbose_name_plural = 'سایز ها'
        verbose_name = 'سایز'
class Color(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'رنگ ها '
        verbose_name = 'رنگ'
class Price(models.Model):
    price = models.CharField(max_length=100)

    def __str__(self):
        return self.price

    class Meta:
        verbose_name_plural = 'قیمت ها'
        verbose_name = 'قیمت'
class Product(models.Model):
    categories = models.ManyToManyField(Category , related_name="products" ,  help_text="دسته بندی" , null=True , blank=True)
    color = models.ManyToManyField(Color, related_name="products" , help_text="رنگ ها" , null=True , blank=True)
    price = models.ManyToManyField(Price, related_name="products", help_text="قیمت" , null=True , blank=True)
    size = models.ManyToManyField(Size , related_name='products' , help_text = "سایز" , null=True , blank=True)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='ProductImage' , null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created',)
        verbose_name = ('کالا')     
        verbose_name_plural = ('کالاها')   
