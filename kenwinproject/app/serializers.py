from .models import Contact
from rest_framework import serializers


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'firstname', 'lastname', 'enterprice', 'number', 'email', 'address']
