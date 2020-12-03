from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout,authenticate,login
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib import messages
# Create your views here.
class ProfileView(LoginRequiredMixin,View):
    template_name = 'Profile/index.html'
    title = 'Profile'

    def get(self,request):
        return render(request,self.template_name,{'title':self.title})

class ProfileLoginView(View):
    tempate_name = 'registration/login.html'
    title = 'Dear Dairy|Login'
    def get(self,request):
        form = AuthenticationForm()
        return render(request,self.tempate_name,{'title':self.title,'form':form})

    def post(self,request):
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            user = authenticate(request,username = form.cleaned_data.get('username'),password=form.cleaned_data.get('password'))
            if user.is_authenticated:
                login(request,user)
                return redirect('memory:home')
        messages.warning(request,'Invalid Username or Password')
        return render(request,self.tempate_name,{'title':self.title,'form':form})

class LogoutView(LoginRequiredMixin,View):
    def get(self,request):    
        logout(request)
        messages.info(request,'You have been logged out successfully!')
        return redirect('profile:login')

class ProfileRegisterView(View):
    template_name = 'registration/register.html'
    success_url = reverse_lazy('memory:home')
    title = 'Dear Dairy|Registration'
    def get(self,request):
        form = UserCreationForm()
        return render(request,self.template_name,{'title':self.title,'form':form})

    def post(self, request):
        """
        for post of UserCreationForm in form
        """
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect(self.success_url)
        return render(request,self.template_name,{'title':self.title,'form':form})