from django.urls import path
from django.views.generic import TemplateView
from django.views.generic.base import View
from . import views

app_name = "blog"

urlpatterns = [
    # path('', TemplateView.as_view(template_name="db.html")),    
    # path('', TemplateView.as_view(template_name="index.html")),    
    path('', views.home, name='Homepage'),    
    path('single/<slug:slug>', views.single, name='Single'),    
]