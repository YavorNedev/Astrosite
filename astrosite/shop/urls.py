from django.urls import path
from astrosite.shop import views

urlpatterns = [
    path('', views.shop_view, name='shop'),
    path('create/', views.create_shop_item, name='create_shop_item'),
    path('buy/<int:pk>/', views.buy_item, name='buy_item'),
]
