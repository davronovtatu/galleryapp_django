from django.shortcuts import render, redirect
from .models import Category,Gallery
from .forms import PhotoaddForm


def home(request):
    categories=Category.objects.all()
    photos=Gallery.objects.all()
    context={
        "categories":categories,
        "photos":photos,
    }
    return render(request,"home.html",context)





def addedphotoview(request):
    if request.method=="POST":
        forms=PhotoaddForm(request.POST,files=request.FILES)
        if forms.is_valid():
            forms.save()
            return redirect("main")
    forms = PhotoaddForm()
    context = {
            "forms": forms,
        }
    return render(request, "addedphoto.html", context)

