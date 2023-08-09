from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import todoform
from . models import todo
from django.views.generic import ListView, UpdateView, DeleteView
from django.views.generic import DetailView
# Create your views here.
class tasklistiew(ListView):
    model = todo
    template_name = 'home.html'
    context_object_name = 'task1'

class taskdetailview(DetailView):
    model = todo
    template_name = 'detail.html'
    context_object_name = 't'

class taskupdateview(UpdateView):
    model = todo
    template_name = 'update.html'
    context_object_name = 't'
    fields=('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('todoapp:ldetail',kwargs={'pk':self.object.id})


class taskdeleteview(DeleteView):
    model=todo
    template_name = 'delete.html'
    success_url = reverse_lazy('todoapp:home')
def add(request):
    task1=todo.objects.all()
    if request.method=='POST':
        name=request.POST.get('todo','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        todo1=todo(name=name,priority=priority,date=date)
        todo1.save()

    return render(request,'home.html',{'task1':task1})

def delete(request,todoid):
    a=todo.objects.get(id=todoid)
    if request.method=='POST':
        a.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    task=todo.objects.get(id=id)
    f=todoform(request.POST or None, instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'task':task,'f':f})