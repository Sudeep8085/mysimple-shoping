
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('details/<pid>/', views.details), # ,id get karne ke liye <id> variable create karna
]


# def myfun(request,id=None):
#     pass
#
# myfun("details/<pid>")
