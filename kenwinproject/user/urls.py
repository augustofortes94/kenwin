from django.urls import path, include
from .views import RegisterUser

app_name = 'user'

urlpatterns = [
    # USERS
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', RegisterUser.register, name='register'),
]