from django.urls import path, include
from rest_framework.authtoken import views as auth_token_views
from . import views
urlpatterns = [
    path('users/', include('users.urls')),
    path('token-auth/', auth_token_views.obtain_auth_token, name='api-token-auth'),
    path('generate-qr/', views.generate_qr )
    ]