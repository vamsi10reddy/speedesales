from django.urls import path, include
from core.views import index
from .views import *

app_name = 'core'

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing'),  # Landing page view
    path("index/", index, name='index'),  # Make sure to use the view function, not a string
    path("products/", product_list_view, name='product-list'),  # Make sure to use the view function, not a string
    path('category/<str:category_name>/', products_by_category, name='products_by_category'),
]
