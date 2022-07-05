from django.shortcuts import render
from django.views.generic import ListView
from .models import Contact
from django.core.paginator import Paginator


class ContactView(ListView):
    def contactList(request):
        if request.method == "POST":
            contacts = Contact.objects.filter(firstname__icontains=request.POST['searched']).order_by('firstname')
        else:
            contacts = Contact.objects.all().order_by('firstname')

        paginator = Paginator(contacts, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'crud_contacts/contact_list.html', {'page_obj': page_obj})
