from django.urls import path
from .views import home, about


urlpatterns = [
    path('', home, name='start'),
    path('about/', about, name='about'),
]