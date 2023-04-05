from CBV_APP import views
from django.urls import path, re_path

app_name = "CBV_APP"

urlpatterns = [
    path("", views.SchoolListView.as_view(), name="list"),
    re_path(r"^(?P<pk>[-\w]+)/$", views.SchoolDetailView.as_view(), name="detail"),
]
