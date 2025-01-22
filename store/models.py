from django.db import models
from django.contrib.auth.models import user

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
    

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    
    image = models.ImageField(upload_to="barnd_image")

    def __str__(self):
        return self.name    


class  ImageFiled(models.Model):
    image = models.ImageField(upload_to="product_images")



class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    display_image = models.ImageField(upload_to="product_display_images")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    # images = models.ManyToManyField(ImageFiled)
    quantity = models.PositiveIntegerField()
    uploaded_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-uploaded_at']

    def __str__(self):
        return self.name

class CartItem(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    @property
    def cost(self):
        return self.product.price * self.quantity
        
    
class Cart(models.model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(user, on_delete=models.CASCADE)
    product_item = models.ForeignKey(CartItem, on_delete=models.CASCADE)
    
    @property
    def total_cost(self):
        return self.product_item.cost
        

