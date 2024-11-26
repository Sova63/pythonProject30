from django.shortcuts import render,HttpResponse
from .models import User, SysUser
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from .forms import UserForm

@login_required(login_url="auth")
def home(request):
	sys_user = request.user
	user = User.objects.get(sys_user = sys_user.id)
	return HttpResponse(f"Привет{user.username}")

def reg(request):
	if request.method =="POST":
		form = UserForm(request.POST)
		user = User()
		sys_user = SysUser()
		sys_user.username = form.data.get('username')
		sys_user.set_password = form.data.get('password')
		sys_user.save()
		user.sys_user = sys_user
		user.first_name = form.data.get('first_name')
		user.last_name = form.data.get('last_name')
		user.save()
	form = UserForm()
	return render(request,'reg.html',{"form":form})
def auth(request):
	if request.method ==  "POST":
		form = UserForm(request.POST)
		user = authenticate(request,form.data.get('username'),form.data.get('password'))
		if user is not None:
			login(request,user)
			return HttpResponse("AuthSucess")
		else:
			return HttpResponse("Auth not sucseed")
	form = UserForm()
	return render(request, 'auth.html',{'form':form})



# Create your views here.
