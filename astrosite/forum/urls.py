from django.urls import path
from astrosite.forum import views

urlpatterns = [
    path('', views.category_list_view, name='category_list'),
    path('category/<int:category_id>/', views.thread_list_view, name='thread_list'),
    path('category/<int:category_id>/create/', views.create_thread_view, name='create_thread'),
    path('thread/<int:thread_id>/', views.thread_detail_view, name='thread_detail'),
]