from django.shortcuts import render,render_to_response
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from single.models import Blog
# Create your views here.
def index(request):
    posts = Blog.objects.all().order_by('-id')[:3]
    # abc = {'posts':posts}
    # print(abc[0].title)
    # print(abc)
    
    return render(request,'index.html',{'whatever':posts})
    # return render_to_response()

def mail(request):
    # print(request.POST.get('message'))
    # print(request.POST.get('name'))
    # print(request.POST.get('app-date')) #address
    # print(request.POST.get('phone'))
    a = 'name:'+ request.POST.get('name') + ' phone:'+request.POST.get('phone') + ' address:'+request.POST.get('app-date') + ' message:'+request.POST.get('message')
    email = EmailMessage('new customer:', a,'', to=['sushil79g@gmail.com'])
    # return HttpResponseRedirect(reverse('single'))