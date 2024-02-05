from django.urls import path
from . import views # importing views from blog application

urlpatterns = [
    path('', views.post_list, name='post_list'),
]
