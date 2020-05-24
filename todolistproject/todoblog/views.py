from django.shortcuts import render, redirect
from .models import Todolist, Comment 
import datetime


#Create your views here.
def home(request):
    todolists = Todolist.objects.all().order_by('deadline')
    return render(request, 'home.html', {'todolists':todolists})

def new(request):
    if request.method == "POST":
        new_todolist = Todolist.objects.create(
            title=request.POST['title'],
            content=request.POST['content'],
            deadline=request.POST['deadline']
        )
        return redirect('detail',new_todolist.pk )
    # else:
    return render(request,'new.html')

def detail(request,todolist_pk):
    todolist = Todolist.objects.get(pk=todolist_pk)

    if request.method =="POST":
        Comment.objects.create(
            post = todolist,
            content = request.POST['content']
        )
        return redirect('detail', todolist_pk)

    return render(request, 'detail.html', {'todolist':todolist})

def edit(request,todolist_pk):
    todolist = Todolist.objects.get(pk=todolist_pk)
    
    if request.method == "POST":
        Todolist.objects.filter(pk=todolist_pk).update(
            title = request.POST['title'],
            content = request.POST['content'],
            deadline=request.POST['deadline']
        )
        return redirect('detail',todolist_pk)
    
    return render(request, 'edit.html',{'todolist':todolist})
    
def delete(request,todolist_pk):
    todolist = Todolist.objects.get(pk=todolist_pk)
    todolist.delete()
    return redirect('home')

def delete_comment(request, todolist_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('detail', todolist_pk)



