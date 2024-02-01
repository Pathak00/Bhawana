from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Poem
import random

# Create your views here.

# def webpage(request):
#     all_poems = Poem.objects.all
#     return render(request,'webpage.html',{'all':all_poems})

# views.py


def aakash(request):
    return render(request,'aakash.html')

# def rang(request):
#     return render(request,'rang.html')

def contact(request):
    return render(request,'contact.html')


# def rang(request, pk):
#     poem = get_object_or_404(Poem, pk=pk)
#     return render(request, 'rang.html', {'poem': poem})

def rang(request, pk, return_webpage=False):
    poem = get_object_or_404(Poem, pk=pk)

    if return_webpage:
        poems = Poem.objects.all()
        return render(request, 'webpage.html', {'poems': poems})
    else:
        return render(request, 'rang.html', {'poem': poem})

def webpage(request):
    poems = Poem.objects.all()
    return render(request, 'webpage.html', {'poems': poems})

# def random_poem_view(request):
#     # Get all poem titles from the database
#     all_poems = Poem.objects.all()

#     # Randomly select one poem
#     random_poem = random.choice(all_poems)

#     return render(request, 'random_poem.html', {'random_poem': random_poem})