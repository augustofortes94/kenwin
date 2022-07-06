from django.urls import path
from .views import ContactView, ContactAPI
from user.views import ApiLogin


urlpatterns = [
    path('', ContactView.contactList, name='contact_list'),
    path('contact/addform', ContactView.contactAddForm, name='contact_addform'),
    path('contact/add', ContactView.contactAdd, name='contact_add'),
    path('contact/delete/<int:id>', ContactView.contactDelete, name='contact_delete'),
    path('contact/list', ContactView.contactList, name='contact_list'),

    # API
    path('api/login/', ApiLogin.as_view(), name='api_login'),
    path('api/contacts/', ContactAPI.as_view(), name='api_contact_list'),
]