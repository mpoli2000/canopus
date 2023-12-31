from django.urls import path
from .views import UserRegisterView, UserEditView, CustomPasswordChangeView, ShowProfilePageView, EditProfilePageView, CreateProfilePageView
from . import views

app_name = 'members'
urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('password/', CustomPasswordChangeView.as_view(), name='password_change'),
    path('password_success/', views.password_success, name='password_success'),
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='show_profile_page'),
    path('<int:pk>/edit_profile_page', EditProfilePageView.as_view(), name='edit_profile_page'),
    path('create_profile_page', CreateProfilePageView.as_view(), name='create_profile_page')
]