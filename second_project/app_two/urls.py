from app_two import views
from django.urls import re_path

urlpatterns = [re_path(r"^$", views.help, name="help")]
