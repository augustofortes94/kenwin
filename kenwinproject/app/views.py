from django.shortcuts import redirect, render
from django.views.generic import ListView
from .models import Contact
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages


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
