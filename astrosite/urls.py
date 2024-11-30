from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('astrosite.main.urls')),
    path('accounts/', include('astrosite.accounts.urls')),
    path('posts/', include('astrosite.posts.urls')),
    path('shop/', include('astrosite.shop.urls')),
    path('forum/', include('astrosite.forum.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


