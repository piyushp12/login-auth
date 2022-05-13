
from django.shortcuts import render, HttpResponse
from base.models import Index
# Create your views here.
def index(request):
    if request.method=="POST":
        name = request.POST['name']
        last = request.POST['name']
        user = request.POST['user']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        confirm = request.POST['confirm']
        Address = request.POST['Address']
        image = request.POST['image']
        index = Index.objects.create(name=name, last=last, email=email, phone=phone, user=user, password=password, confirm=confirm, Address=Address, image=image)
        index.save()

    return render(request, 'index.html')

def Doctor(request):
    return render(request, 'Doctor.html')

def Patient(request):
    return render(request, 'Patient.html')