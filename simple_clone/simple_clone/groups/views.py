from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView

from groups.models import Group, GroupMember


# Create your views here.
class CreateGroup(LoginRequiredMixin, CreateView):
    fields = ("name", "description")
    model = Group


class SingleGroup(DetailView):
    model = Group


class ListGroups(ListView):
    model = Group
