from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("<em> My second project</em>")


# Create your views here.


def help(request):
    context = {"help_insert": "HELP PAGE using variable template"}
    return render(request, context=context, template_name="app_two/help.html")
