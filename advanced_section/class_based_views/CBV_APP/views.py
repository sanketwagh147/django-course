from typing import Any, Dict

from CBV_APP.models import School, Student
from django.shortcuts import HttpResponse, render

# Create your views here.
from django.views.generic import DeleteView, DetailView, ListView, TemplateView, View

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
