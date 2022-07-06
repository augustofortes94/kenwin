from .models import Contact
from .serializers import ContactSerializer
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from user.decorators import api_login_required


class ContactView(ListView):
    @login_required
    def contactAdd(request):
        Contact.objects.create(
            firstname=request.POST['firstname'],
            lastname=request.POST['lastname'],
            enterprice=request.POST['enterprice'],
            number=request.POST['number'],
            email=request.POST['email'],
            address=request.POST['address'],
        )
        messages.success(request, request.POST['firstname'] + ' ha sido creado')
        return redirect('/contact/list')

    @login_required
    def contactAddForm(request):
        return render(request, 'crud_contacts/contact_add.html')
    
    @login_required
    def contactDelete(request, id):
        contact = Contact.objects.get(id=id)
        Contact.objects.filter(id=id).delete()
        messages.success(request,  contact.firstname + ' ha sido eliminada')
        return redirect('/contact/list')

    @login_required
    def contactList(request):
        if request.method == "POST":
            contacts = Contact.objects.filter(firstname__icontains=request.POST['searched']).order_by('firstname')
        else:
            contacts = Contact.objects.all().order_by('firstname')

        paginator = Paginator(contacts, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'crud_contacts/contact_list.html', {'page_obj': page_obj})


class ContactAPI(APIView):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    @api_login_required
    def get(self, request, *args, **kwargs):
        return Response({'message': "Success", 'contacts': list(Contact.objects.values())}, status=status.HTTP_200_OK)

    @api_login_required
    def post(self, request, *args, **kwargs):
        contact = Contact.objects.create(
            firstname=request.data['firstname'],
            lastname=request.data['lastname'],
            enterprice=request.data['enterprice'],
            number=request.data['number'],
            email=request.data['email'],
            address=request.data['address'],
        )
        serializer = ContactSerializer(data={'firstname': contact.firstname, 'lastname': contact.lastname, 'enterprice': contact.enterprice, 'number': contact.number, 'email': contact.email, 'address  ': contact.address})
        serializer.is_valid(raise_exception=True)
        return Response({'message': "Success", 'contact': serializer.data}, status=status.HTTP_202_ACCEPTED)
