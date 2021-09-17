from django.urls import path

from catalogo.views import HomeListView


urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
]
