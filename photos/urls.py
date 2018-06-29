from django.urls import path
from django.views.generic import DetailView, ListView

from .models import Gallery

urlpatterns = [
    path('', ListView, 
    name="gallery_list"
    ),
    path('<slug:slug>/', DetailView,
        {
            'queryset': Gallery.published_objects.all(),
            'template_name': "galleries/gallery_detail.html"
        },
        name="gallery_detail"
    ),
]
