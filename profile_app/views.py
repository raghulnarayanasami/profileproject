from django.shortcuts import render
from .models import ProfileData
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate,login, logout
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
import os

# Create your views here.
def get_hostname():
    out = os.popen('hostname').read()
    return str(out)

def page_not_found_view(request, exception):
    return render(request, 'profile_app/error_404.html')

def dashboard(request):
    data = get_hostname()
    return render(request, 'profile_app/dashboard.html', {"data": data})

@csrf_exempt
def profile_create(request):
    data = get_hostname()
    if request.method == "POST":
        ''' getting data from user form'''
        name = request.POST['emp_name']
        emp_id = request.POST['emp_id']
        phone_number = request.POST['phone_number']
        print(name, emp_id, phone_number)
        ''' storing data into database'''
        profileData = ProfileData.objects.create(
            name=name,
            emp_id=emp_id,
            phone_number=phone_number,
        )
        profileData.save()
        return HttpResponseRedirect(reverse("profile_data"))
    else:
        return render(request, "profile_app/profile_create.html", {"data": data})

@csrf_exempt
def profile_data(request):
    data = get_hostname()
    '''filtering data based on user_login'''
    emp_data = ProfileData.objects.all()
    return render(request, "profile_app/profile_view.html", {"data": data, "emp_data": emp_data})

