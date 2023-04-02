from django.shortcuts import render

# Create your views here.
APP = "templates_app"


def index(request):
    context = {
        "title": "my first djanog application",
        "footer": "Sanket Corp pvt",
        "footer_right": "THis is index in index page",
    }
    return render(request, f"{APP}/index.html", context=context)


def other(request):
    return render(request, f"{APP}/other.html")


def relative(request):
    return render(request, f"{APP}/relative_url_templates.html")
