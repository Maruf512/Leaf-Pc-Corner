from django.shortcuts import render, HttpResponse


def home(request):
    if(request.POST):
        login_data = request.POST.dict()
        username = login_data.get("input_user_name")
        password = login_data.get("input_user_password")
        print(username, password)
        if username and password != "":
            return HttpResponse("Login Successful.")
        else:
            return render(request, "login.html")
    else:
        return render(request, "login.html")


