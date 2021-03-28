from django.shortcuts import render
from django.http import HttpResponse #odpowiedź dla przeglądarki
# Create your views here.
import datetime

def hello(request):
    my_context = {"time": datetime.datetime.now()}
    return render(request, template_name="index.html", context=my_context) 

def index(request):
     return render(request, template_name="base.html") 
     
def subpage(request):
     return render(request, template_name="subpage.html") 

from movies.models import Movie

def list_movies(request):
    # pylint: disable=no-member
    my_context = {"movies": Movie.objects.all()}
    return render(request, template_name="movie_list.html", context=my_context) 

def my_profile(request):
     return render(request, template_name="my_profile.html")

from django.contrib.auth.forms import UserCreationForm

def user_signup(request):
     if request.method == 'POST' :
          #przetwarzanie formularza
          form = UserCreationForm(request.POST)
          if form.is_valid():
               form.save()
               return render(request, template_name="registration/signup_complete.html")
     else: 
          # nowy formularz, czysty
          form = UserCreationForm()

     return render(request, template_name="registration/signup.html",
     context={'form':form})
