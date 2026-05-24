# Amazon Template (Django E-commerce Storefront)

This project is a Django-based web application designed as a flexible e-commerce template. It mirrors the layout and data-delivery patterns of modern online marketplaces like Amazon, utilizing a modular structure to manage various types of retail content.

## Project Overview
The project is built to handle a dynamic storefront, featuring product catalogs, interactive cards, carousels, and dedicated content pages. It is structured as a single Django application (`store`) within a core project (`myproject`).

## Key Features
* **Dynamic Product Catalog**: Manage products with pricing, previous pricing, and sale status.
* **Modular UI Components**:
    * **Cards**: Grid-based content containers.
    * **Carousels**: Product carousels for showcasing items in an interactive, sliding interface.
* **Integrated Pages**:
    * **Shop**: A full product listing page.
    * **About**: Dynamic "About Us" content section.
    * **Contact**: Dedicated contact page.
* **Polymorphic Routing**: Uses a single, versatile view function to handle product details across different data models (shop, card, carousel).

## Project Architecture

### Data Models (`store/models.py`)
* **Product**: Core catalog item with metadata.
* **Card & CardItem**: Containers and items for grid-style layouts.
* **ProductCarousel & ProductCarouselItem**: Models for interactive product rotators.
* **AboutFirst & AboutSecond**: Structured content models for the About page.

### View Logic (`store/views.py`)
* **Index**: Aggregates cards and carousels, bundling them into a structured row format (4 cards per 2 carousels).
* **Product Detail**: A generic view that dynamically fetches data based on the requested model type (shop, card, or carousel).

### URL Mapping (`store/urls.py`)
Provides clear paths for the index, shop, about, and contact pages, along with a dynamic URL pattern for products: `product/<model>/<int:pk>/`.

## Installation & Setup

1. **Prerequisites**: Ensure you have Python installed.
2. **Clone the repository**:
```bash
   git clone <repository-url>
   cd <project-directory>
3. **Environment Setup**:

Bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
4. **Install Dependencies**:

Bash
   pip install django
5. **Database Migration**:

Bash
   python manage.py migrate
6. **Run the Server**:

Bash
   python manage.py runserver
Navigate to http://127.0.0.1:8000/ to view the application.

Configuration (myproject/settings.py)
Database: Uses sqlite3 for local development.

Static Assets: CSS files are served from the global static/css/ directory.

Apps: The store app is configured as store.apps.StoreConfig.

Built with Django.