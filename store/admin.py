from django.contrib import admin
from .models import Product, Carousel, Card, CardItem, ProductCarousel, ProductCarouselItem, AboutFirst, AboutSecond


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "prev_price", "sale")
    search_fields = ("name",)
    
admin.site.register(Carousel)

class CardItemInline(admin.TabularInline):
    model = CardItem
    extra = 0
    max_num = 4
    verbose_name = "Card Item"
    verbose_name_plural = "Card Items"


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ("title",)
    inlines = [CardItemInline]
    
class ProductCarouselItemInline(admin.TabularInline):
    model = ProductCarouselItem
    extra = 1

@admin.register(ProductCarousel)
class ProductCarouselAdmin(admin.ModelAdmin):
    list_display = ("title",)
    inlines = [ProductCarouselItemInline]
    

admin.site.register(AboutFirst)
admin.site.register(AboutSecond)