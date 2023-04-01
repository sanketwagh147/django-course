from django.shortcuts import render
from third_app.forms import NewUserForm
from third_app.models import User

# Create your views here.


def index(request):
    return render(request, "third_app/index.html")


# def users(request):

#     user_list = User.objects.order_by("first_name")
#     context = {"users": user_list}

#     return render(request, "third_app/users.html", context=context)


def users(request):

    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("Error invalid form")

    return render(request, "third_app/users.html", {"form": form})
