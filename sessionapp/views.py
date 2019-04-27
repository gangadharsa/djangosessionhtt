from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def input(request):
    return render(request,'base.html')
def add(request):
    x=int(request.POST['t1'])
    y=int(request.POST['t2'])
    z=x+y
    request.session['z']=z
    request.session.set_expiry(60)
    return HttpResponse("<html><body bgcolor=red><h1>Data Submitted Successfully</h1></body></html>")
def display(request):
    if request.session.has_key('z'):
        z=request.session['z']
        return HttpResponse("<html><body bgcolor=yellow><h3>The sum Of Two no is:</h3></body></html>"+str(z))
    else:
        return render(request,'base.html')

