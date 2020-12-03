from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse_lazy
from .models import Memory,MemoryForm
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
# Create your views here.

class MemoryListView(LoginRequiredMixin,generic.ListView):
    template_name = 'memory/index.html'
    context_object_name = 'memories'
    model = Memory
    title = 'Memories'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.title
        return context
    
class MemoryCreateView(LoginRequiredMixin,generic.CreateView):
    template_name = 'memory/memory_create.html'
    model = Memory
    fields = ['title','desc']
    title = 'New Memory'
    success_url = reverse_lazy('memory:home')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.title
        return context
    
    def form_valid(self,form):
        form.instance.user = self.request.user
        return super(MemoryCreateView,self).form_valid(form)

class MemoryDeleteView(LoginRequiredMixin,generic.View):
    def get(self,request,pk=None):
        if pk:
            memory = get_object_or_404(Memory,pk=pk)
            memory.delete()
            messages.success(request,f'{memory.title} deleted successfully')
            return redirect('memory:home')
        messages.warning(request,message='there was as error processing this request'.capitalize)
        return redirect('memory:home')        

class MemoryEditView(LoginRequiredMixin,generic.UpdateView):
    template_name = 'memory/memory_edit.html'
    success_url = reverse_lazy('memory:home')
    model = Memory
    fields = [
        'title',
        'desc',
    ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'edit memory'.capitalize
        return context
    