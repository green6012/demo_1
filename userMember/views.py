from django.http import HttpResponse
from django.shortcuts import render, redirect
from  .forms import registerForm,loginForm
from  django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import CreateUserForm
from  django.contrib import messages

# Create your views here.
# class registerUser(View):
#     def get(self,request):
#         rF = registerForm
#         return  render(request, 'userMember/register.html', {'rF': rF})
#
#     def post(self,request):
#         username = request.POST['username']
#         email = request.POST['email']
#         password = request.POST['password']
#         user = User.objects.create_user(username,email,password)
#         user.save()
#         return HttpResponse('save user success')


def register(request):
    rF = CreateUserForm()
    if request.method == "POST":
        rF = CreateUserForm(request.POST)
        if rF.is_valid():
            rF.save()
            return redirect('userMember:loginUser')
    return render(request, 'userMember/register.html', {'rF': rF})

# class loginUser(View):
#     def get(self,request):
#         lU = loginForm
#         return render(request, 'userMember/login.html',{'lU':lU})
#     def post(self,request):
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             # Redirect to a success page.
#             return render(request,'userMember/private.html')
#         else:
#             # Return an 'invalid login' error message.
#            return  HttpResponse('fail')
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('realcam:index')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('realcam:index')

        else: messages.error(request,'your username or password is not correct')
    return render(request,'userMember/login.html')

def logoutUser(request):
    logout(request)
    # return render(request, 'polls/base.html')
    return redirect('polls:home')

#
# @login_required(login_url="/login/")
# def privateWeb(request):
#     return render(request, 'realcam/video.html')