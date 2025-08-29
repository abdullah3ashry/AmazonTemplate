from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=255)
    prev_price = models.DecimalField(decimal_places=2, max_digits=255)
    sale = models.CharField(max_length=255)
    image = models.TextField()
    claimed = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Carousel(models.Model):
    image = models.TextField()
    
class Card(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class CardItem(models.Model):
    name = models.CharField(max_length=255, default="Product")
    card = models.ForeignKey(Card, related_name="items", on_delete=models.CASCADE)
    image = models.TextField() 
    label = models.CharField(max_length=100, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=255, default=9.99)

    def __str__(self):
        return f"{self.label} ({self.card.title})"


class ProductCarousel(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class ProductCarouselItem(models.Model):
    carousel = models.ForeignKey(ProductCarousel, related_name="items", on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default="Product")
    image = models.TextField()
    label = models.CharField(max_length=200, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=255, default=9.99)

    def __str__(self):
        return f"{self.label or 'Item'} ({self.carousel.title})"
    

class AboutFirst(models.Model):
    image = models.TextField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    def __str__(self):
        return self.title
    

class AboutSecond(models.Model):
    image = models.TextField()
    title = models.CharField(max_length=255)
    date = models.TextField()
    def __str__(self):
        return self.title