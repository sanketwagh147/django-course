from django.urls import re_path
from third_app import views

urlpatterns = [re_path("^$", views.users, name="users")]
