from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from api import views


app_name = "api"

urlpatterns = [
    path("api/hello/", views.HelloAPIView.as_view(), name="hello"),
    path("api/token-auth/", obtain_auth_token, name="token_auth"),
]
