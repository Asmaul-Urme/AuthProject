from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.view import  Views
#import the User class (model) 
from django.models import User
#import the RegitrationForm from forms.py
from .forms import RegistrationForm






# Create your views here.
def resister_view(request):
  if request.method == "POST":
    form = RegistrationForm(request.POST)
    if form.is_valid():
      username = form.cleaned_data.get("username")
      password = form.cleaned_data.get("password")
      user = User.objects.create_user(username=username,password=password)
      login(request, user)
      return redirect('home')
  else:
    form = RegistrationForm()
    return render(request, 'accounts/register.html',{'form'.form} )



def login_view(request):
  if request.method == "POST":
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username,password=password)
    if user is not None:
      login(request,user)
      request.POST.get('next') or request.GET.get('next') or 'home'
      return redirect(next_url)

    else:
      error_message = "Invalid Credentials"
  return render(request, 'acciunts/login.html',{'error':error_message})

def logout_view(request):
  if request.method =="POST":
    logout(request)
    return redirect('login')
  else:
    return redirect('home')


#Homeview
#Using the decoratoe
@login_required
def home_view(request):
  return render(request,'home/home.html')
#protected view
class ProtectedView(LoginRequiredMixin,Views):
  login_url ='/login/'
  #'next ' - to redirect URL
  redirected_field_name = 'redirect_to'

  def get(self,request):
    return render(request, 'registration/protected.html')