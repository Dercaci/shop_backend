from django.db import models



class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    description = models.TextField(blank=True)
        
    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return self.name


class WishList(models.Model):
    owner = models.ForeignKey('auth.User', related_name='wishlist', on_delete = models.CASCADE)
    product = models.ManyToManyField(Product)
    name = models.CharField(max_length=50)


    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
