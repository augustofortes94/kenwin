from django.urls import path, include
from .views import ContactView


urlpatterns = [
    path('', ContactView.contactList, name='contact_list'),
    path('contact/addform', ContactView.contactAddForm, name='contact_addform'),
    path('contact/add', ContactView.contactAdd, name='contact_add'),
    path('contact/delete/<int:id>', ContactView.contactDelete, name='contact_delete'),
    path('contact/list', ContactView.contactList, name='contact_list'),
]