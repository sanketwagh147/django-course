from typing import Any, Dict

from CBV_APP.models import School, Student
from django.shortcuts import HttpResponse, render
from django.urls import reverse, reverse_lazy

# Create your views here.
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
    View,
)

""" # Function based views 
def index(request):
    return render(request, "index.html")
 """


"""
# View Class based Response
class CBView(View):
    def get(self, request):
        return HttpResponse(
            ""<head><link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css"
              rel="stylesheet"
              integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC"
              crossorigin="anonymous"></head>
              <div class='container'><h1>Class based vies example </h1></div>""
        )
 """


class IndexView(TemplateView):
    template_name = "index.html"


# ⭐ by default it will return school_list as variable to template to override use above
class SchoolListView(ListView):
    """This will provide all the list of all items"""

    # override default <model>_list(variable passed to template)
    context_object_name = "schools"

    model = School
    template_name = "school_list.html"


class SchoolDetailView(DetailView):
    """This will provide all the list of all items"""

    # DetailView returns lower case version of class to override it
    # we can use :-
    context_object_name = "school_detail"
    model = School
    template_name = "school_detail.html"


class SchoolCreateView(CreateView):
    fields = ("name", "principal", "location")
    model = School
    template_name = "school_form.html"


class SchoolUpdateView(UpdateView):
    fields = ("name", "principal")
    model = School
    template_name = "school_form.html"


class SchoolDeleteView(DeleteView):
    model = School
    success_url = reverse_lazy("CBV_APP:list")
    template_name = "school_confirm_delete.html"
