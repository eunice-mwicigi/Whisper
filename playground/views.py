from django.views.generic import CreateView
from saturdayWeb.models import CustomUser
from .form import CustomUserCreationForm
from  django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

#create your views here.

from django.http import HttpResponse

def say_hello(request):
   return HttpResponse()

def calculation(a,b):
    x = a+b
    return (x)




class SignUp(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("none")
    template_name = "register.html"

