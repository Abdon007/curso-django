from django.shortcuts import render


def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'name' : 'Abdon França',
    })

# Create your views here.
