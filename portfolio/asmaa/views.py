from django.shortcuts import render
from .models import Home , About, Profile ,Category,Portfolio

def index(request):

    home=Home.objects.latest('time')

    about=About.objects.latest('time')
    profile=Profile.objects.filter(about=about)

    category=Category.objects.all()

    portfolio=Portfolio.objects.all()



    context={
        'home':home,
        'profile':profile,
        'about':about,
        'category':category,
        'portfolio':portfolio,



    }

    return render(request,'index.html',context)
 