from django.urls import path
from user_registration_app import views

urlpatterns = [
    path('info/', views.user_info, name='user_info'),
    path('signup/', views.user_signup, name='user_signup')
]
