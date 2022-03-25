from django.urls import path
from app1 import views
from app2.views import hello_there

urlpatterns = [
    path("base/", views.base, name='base'),
    path("", views.index, name='index')
]
