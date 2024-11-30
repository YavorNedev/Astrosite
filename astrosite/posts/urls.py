from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from astrosite.posts import views

urlpatterns = [
    path('', views.posts_list_view, name='posts_list'),
    path('create/', views.post_create_view, name='post_create'),
    path('<int:pk>/', views.post_detail_view, name='post_detail'),
    path('posts/edit/<int:pk>/', views.post_edit_view, name='post_edit'),
    path('posts/delete/<int:pk>/', views.post_delete_view, name='post_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
