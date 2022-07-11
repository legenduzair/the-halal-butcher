from django.shortcuts import render


def profile(request):
   
    template = 'profile.html'
    context = {}

    return render(request, template, context)