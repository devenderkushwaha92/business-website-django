from django.shortcuts import render,redirect
from .forms import contactform
from django.http import HttpResponse
from django.contrib import messages


def get_name(request):
    form = contactform(request.POST)
    success = False;
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            messages.success(request, 'Form submission successful')
            form = contactform()
            success = True;

    # if a GET (or any other method) we'll create a blank form
    else:
        form = contactform()

    return render(request, "home.html", {"form": form})

# def home(request):
#     return render(request,"home.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")


