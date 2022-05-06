from django.shortcuts import render,redirect
from .models import *
from .forms import *


def home(request):
    list=List.objects.all()
    form=ListForm()
    if request.method=='POST':
        form=ListForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context={'list':list,'form':form}
    return render(request,'todobase/home.html',context)

    

def updateList(request,rp):
    list=List.objects.get(id=rp)
    form=ListForm(instance=list)

    if request.method=='POST':
        form=ListForm(request.POST,instance=list)
        if form.is_valid():
            form.save()
        return redirect('/')


    context={'form':form}
    return render(request,'todobase/update_list.html',context)


def deleteList(request,rp):
    item=List.objects.get(id=rp)

    if request.method=='POST':
        item.delete()
        return redirect('/')
        
    context={'item':item}
    return render(request,'todobase/delete.html',context)




