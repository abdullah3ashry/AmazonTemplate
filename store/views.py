from django.shortcuts import render, get_object_or_404
from .models import Product, Carousel, Card, CardItem, ProductCarousel, ProductCarouselItem, AboutFirst, AboutSecond

# Create your views here.
def index(request):
    carousels = Carousel.objects.all()
    cards = list(Card.objects.prefetch_related("items").all())
    product_carousels = list(ProductCarousel.objects.prefetch_related("items").all())
    rows = []
    carousel_index = 0
    for i in range(0, len(cards), 4):
        row_cards = cards[i:i+4]
        row_carousels = product_carousels[carousel_index:carousel_index+2]
        rows.append({"cards": row_cards, "carousels": row_carousels})
        carousel_index += 2

    return render(request, 'store/Index.html', {'carousels': carousels, 'rows': rows})


def shop(request):
    products = Product.objects.all()
    return render(request, 'store/Shop.html',{'products': products})

def contact(request):
    return render(request, 'store/Contact.html')

def product(request, pk, model):
    if model == "shop":
        product = get_object_or_404(Product, pk=pk)
        source = "shop"
    elif model == "card":
        product = get_object_or_404(CardItem, pk=pk)
        source = "card"
    elif model == "carousel":
        product = get_object_or_404(ProductCarouselItem, pk=pk)
        source = "carousel"
    else:
        raise ValueError("Unknown product model")
    
    return render(request, "store/Product.html", {
        "product": product,
        "source": source,
    })

def about(request):
    about_first = AboutFirst.objects.all()
    about_second = AboutSecond.objects.all()
    return render(request, 'store/About.html', {
        'about_first': about_first,
        'about_second': about_second
    })