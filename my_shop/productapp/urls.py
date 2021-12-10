
from django.urls import path
from .views import ProductsListView

app_name = 'productapp'

urlpatterns = [
    path('', ProductsListView.as_view(), name='index'),
]
