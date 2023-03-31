from django.shortcuts import render

from first_app.models import AccessRecord, Topic, Webpage

# Create your views here.


def index(request):
    context = {"insert_me": "From views.py file"}
    webpages_list = AccessRecord.objects.order_by("date")
    date_dict = {"access_records": webpages_list}
    return render(request, template_name="first_app/index.html", context=date_dict)


def logos(request):
    context = {"image_url": "static/first_app/logos/forbes.png", "image_name": "forbes"}
    return render(request, template_name="first_app/logos.html", context=context)
