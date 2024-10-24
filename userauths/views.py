from django.shortcuts import render
from  django.http import HttpResponse
from userauths.forms import UserRegisterForm
from django .contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect

def registration_page(request):

    if request.method == "POST":
        form = UserRegisterForm(request.POST or None)
        if form.is_valid():
            new_user = form.save()    
            username = form.cleaned_data.get("username")    
            messages.success(request, f"Hey {username}, Your Account Was Created Successfullly.")
            new_user = authenticate(username = form.cleaned_data.get("email"),  
                                    password = form.cleaned_data.get("password1"))
            login(request, new_user)
            return redirect("core:index")
    else:
        print("User Cannot Be Registered")
        form = UserRegisterForm()


    context = {
        'form': form
    }
    return render(request, 'userauths/sign-up.html', context)