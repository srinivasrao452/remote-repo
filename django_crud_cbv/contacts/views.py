
from django.shortcuts import render
from .models import Contact

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

class ContactList(ListView):
    model = Contact
    # contact_list.html
    # contact_list




class ContactDetail(DetailView):
    model = Contact
    # contact_detail.html
    # contact   or   object





class ContactCreate(CreateView):
    model = Contact
    fields = '__all__'
    # fields = ['name' , 'email']
    # contact_form.html
    # form






class ContactUpdate(UpdateView):
    model = Contact
    fields = '__all__'
    # fields = ['name','email']


class ContactDelete(DeleteView):
    model = Contact
    success_url = reverse_lazy('contact_list')

