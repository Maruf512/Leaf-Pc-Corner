from django.shortcuts import render, HttpResponse
from User.models import User
from werkzeug.security import generate_password_hash, check_password_hash
from django.contrib import messages

def home(request):
    if(request.POST):
        login_data = request.POST.dict()
        username = login_data.get("input_user_name")
        password = login_data.get("input_user_password")
        
        user = User.objects.filter(u_name=username)
        print(user)
        if user:
            user_info = User.objects.filter(u_password=password)
            if user_info:
                return HttpResponse("Login Successful.")
            else:
                return render(request, "login.html")
        else:
            return render(request, "login.html")
    else:
        # x = User.objects.get(id=1)
        # print(x.u_name)
        # print(x.u_password)
        return render(request, "login.html")


