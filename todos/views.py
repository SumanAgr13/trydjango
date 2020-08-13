from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import * 
from .forms import *
def home_view(request,*args,**kwargs):
    items = Items.objects.all()
    form = ItemsForm()

    if request.method == 'POST':
        form= ItemsForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'items':items, 'form':form}
    return render(request,'home.html',context)

def add_view(request, *args,**kwargs):
    return render(request,"add.html",{})
def viewdelete_view(request, pk):
    items= Items.objects.get(id=pk)

    if request.method == 'POST':
        items.delete()
        return redirect('/')

    context = {'items':items}
    return render(request,"viewdelete.html",context)
def viewupdate_view(request, pk):
    items= Items.objects.get(id=pk)
    form = ItemsForm(instance=items)

    if request.method == 'POST':
        form = ItemsForm(request.POST,instance=items )
        if form.is_valid():
            form.save()
        return redirect('/')

    context={'form':form}
    return render(request,"update.html",context)
# Create your views here.
