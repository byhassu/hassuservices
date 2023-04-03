from django.shortcuts import render
from response.models import responseForm

def home(request):
    return render(request,'index.html')
def  contact(request):
    return render(request,'contact.html')
def  about(request):
    return render(request,'about.html')
def response(request):
    if request.method=='POST':
        n=request.POST.get('name')
        e=request.POST.get('email')
        p=request.POST.get('phone')
        d=request.POST.get('desc')
        data=responseForm(name=n,email=e,phone=p,desc=d)
        data.save()


    return render(request,'contact.html')

