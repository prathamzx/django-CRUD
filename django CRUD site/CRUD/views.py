from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .forms import NameForm,Form,DeleteNewForm
from .models import Post

def index(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            form_item=form.save(commit='false')
            form_item.save()
            return redirect('../')
    else:
        form = Form()

    return render(request, 'CRUD/index.html', {'form': form})

def home(request):
    return render(request,'CRUD/home.html')


def update(request):
    form=None
    item=get_object_or_404(Post,username=request.session['name'])
    form=Form(request.POST or None,instance=item)
    if form.is_valid():
        form.save()
        return redirect('../')
    return render(request, 'CRUD/update.html', {'form': form})


def search(request):
    form=None
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            f=form.cleaned_data['username']
            item=get_object_or_404(Post,username=f)
            if not item is None:
                request.session['name']=f
                return redirect('../update')
            else:
                return redirect('../')
    else:
        form = NameForm()

    return render(request, 'CRUD/search.html', {'form': form})

def delete(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            f=form.cleaned_data['username']
            item=get_object_or_404(Post,username=f)
            if not item is None:
                form = DeleteNewForm(request.POST or None,instance=item)
                item.delete()
                return redirect("../")
            else:
                return redirect('../')
    else:
        form = NameForm()

    return render(request, 'CRUD/delete.html', {'form': form})



def read(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            f=form.cleaned_data['username']
            item=get_object_or_404(Post,username=f)
            if not item is None:
                form=Form(instance=item)
                #form.save()
            else:
                return redirect('../')

    else:
        form = NameForm()

    return render(request, 'CRUD/read.html', {'form': form})
