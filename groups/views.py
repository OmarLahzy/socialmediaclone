from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.urls import reverse
from django.views import generic
from groups.models import Group

class CreateGroupeView(LoginRequiredMixin,generic.CreateView):
    fields = ('name','description')
    model = Group

class singleGroupe(generic.DetailView):
    context_object_name = 'group_data'
    model = Group
    template_name = 'groups/group_detial.html'

class ListGroupe(generic.ListView):
    context_object_name = 'Group_list'
    model = Group
