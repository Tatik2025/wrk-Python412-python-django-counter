from django.urls import path
from app_counter import views


app_name = "app_counter"

urlpatterns = [
    path("", views.index, name="index"),
    path("counter/", views.counter, name="counter"),
    path("counter/create/", views.create_counter, name="create_counter"),
    path("counter/increase/<int:counter_id>", views.increase_counter, name="increase_counter"),
    path("counter/decrease/<int:counter_id>", views.decrease_counter, name="decrease_counter"),
    path("counter/delete/<int:counter_id>", views.delete_counter, name="delete_counter"),
    path("counter/favorite/<int:counter_id>", views.is_favorite_counter, name="is_favorite_counter"),

]