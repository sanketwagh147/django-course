from django.shortcuts import render

# Create your views here.


def index(request):
    context = {"insert_me": "From views.py file"}
    return render(request, template_name="first_app/index.html", context=context)


def logos(request):
    context = {"image_url": "static/first_app/logos/forbes.png", "image_name": "forbes"}
    return render(request, template_name="first_app/logos.html", context=context)
