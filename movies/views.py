from django.shortcuts import render
from django.http import HttpResponse #odpowiedź dla przeglądarki
# Create your views here.
import datetime

def hello(request):
    my_context = {"time": datetime.datetime.now()}
    return render(request, template_name="index.html", context=my_context) 

def index(request):
     my_context = {"time": datetime.datetime.now()}
     return render(request, template_name="index.html", context=my_context) 
  
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
     #zwrócenie wyrenderowanego HTMLa
     return render(request, template_name="registration/signup.html",
     context={'form':form})

from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return render(request, template_name="logged_out.html")


def movie_detail(request, movie_id):
     # pylint: disable=no-member
    my_context = {"movie": Movie.objects.get(id=movie_id)}
    return render(request, template_name="movie_detail.html", context=my_context)

from movies.models import Review

def review_list(request):
     # pylint: disable=no-member
    my_context = {"reviews": Review.objects.all()}
    return render(request, template_name="review_list.html", context=my_context)

from movies.models import Movie
from datatableview.views import DatatableView
class ZeroConfigurationDatatableView(DatatableView):
    model = Movie
    template_name = "top_movies.html"