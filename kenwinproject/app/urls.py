from django.urls import path, include
from .views import ContactView


urlpatterns = [
    path('', ContactView.contactList, name='contact_list'),
    path('contact/list', ContactView.contactList, name='contact_list'),
]