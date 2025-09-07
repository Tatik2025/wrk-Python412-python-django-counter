from django.urls import path
from api import views


app_name = "api"

urlpatterns = [
    path("api/hello/", views.HelloAPIView.as_view(), name="hello"),
]
