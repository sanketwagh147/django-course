from basic_form_app import forms
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "basic_form_app/index.html")


def form_name_view(request):
    form = forms.FormName()

    if request.method == "POST":
        form = forms.FormName(request.POST)

        if form.is_valid():
            print(f"{'success validating':-^50}")
            form_data = form.cleaned_data
            for key, value in form_data.items():
                print(f"{key:<10}: {value:>40}")

    return render(request, "basic_form_app/form_page.html", {"form": form})
