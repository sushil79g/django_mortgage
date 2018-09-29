from django.shortcuts import render
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def index(request):
    return render(request,'index.html',context={})

def mail(request):
    # print(request.POST.get('message'))
    # print(request.POST.get('name'))
    # print(request.POST.get('app-date')) #address
    # print(request.POST.get('phone'))
    a = 'name:'+ request.POST.get('name') + ' phone:'+request.POST.get('phone') + ' address:'+request.POST.get('app-date') + ' message:'+request.POST.get('message')
    email = EmailMessage('new customer:', a,'', to=['sushil79g@gmail.com'])
    # return HttpResponseRedirect(reverse('single'))