from django.http.response import HttpResponse
from chat.models import Thread
from django.shortcuts import render
from .models import *

# Create your views here.


def messages_pages(request):
    print("login user..............",request.user)
    threads=Thread.objects.by_user(user=request.user).prefetch_related('chatmessage_thread')
    context={
        'Threads':threads
    }
    print(threads)
    return render(request,'messages.html',context)

def create_thread(request):
    if request.method=='POST':
        other=request.POST['other']
        other_user=User.objects.get(id=other)
        if Thread.objects.filter(Q(first_person=request.user,second_person=other_user) | Q(first_person=other_user,second_person=request.user)).exists():
            
            print(request.user)
            print(other_user.username)
            return HttpResponse("exist")
        else:
            thread_obj=Thread(first_person=request.user,second_person=other_user)
            thread_obj.save()
            print(request.user)
            print(other_user.username)
            return HttpResponse("not exist")    


    user=User.objects.all()
    context={
        'user':user
    }
    return render(request,'create_thread.html',context)    
