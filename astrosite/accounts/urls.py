from django.urls import path
from astrosite.accounts import views
from astrosite.accounts.views import ChangePasswordView, delete_profile_view, logout_view
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    # path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('logout/', logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit/', views.edit_profile_view, name='edit_profile'),
    path('profile/change-password/', ChangePasswordView.as_view(), name='change_password'),
    path('profile/delete/', delete_profile_view, name='delete_profile'),
]