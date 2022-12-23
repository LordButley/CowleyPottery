from django.db import models

# Create your models here.

class Category(models.Model):

    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=254)
    readable_name = models.CharField(max_length=254, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_readable_name(self):
        return self.readable_name

class Product(models.Model):

    name = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.PositiveIntegerField(blank= False, default=0)
    description = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    date_added = models.DateField(auto_now_add=True)
    


    def __str__(self):
        return self.name

class Product_Category(models.Model):
   
    class Meta:
        verbose_name_plural = "Product_Category"

    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    product = models.ForeignKey('Product', null=True, blank=True, on_delete=models.CASCADE)
    
