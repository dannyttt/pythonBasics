from django.urls import path
from . import views

app_name = "bookstore"
urlpatterns = [
    path("", views.home, name="home"),
    path("<int:book_id>/", views.edit, name="edit"),
    path("<int:book_id>/submit/", views.submit, name="submit"),
]
