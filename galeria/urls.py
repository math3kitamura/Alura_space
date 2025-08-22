from django.urls import path
from galeria.views import index

url_patterns = [
    path('', index)
]