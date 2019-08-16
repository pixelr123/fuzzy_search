from django.db.models.functions import Length
from django.shortcuts import render_to_response, render
from django.views.decorators.csrf import csrf_protect
from .models import Word

@csrf_protect
def index(request):
    return render_to_response('base.html')

@csrf_protect
def search_words(request):
    if request.method=='GET':
        word = request.GET['word']
    else:
        word=''
    words = Word.objects.filter(name__contains=word, name__startswith=word).order_by('-frequency')
    words = words.order_by(Length('name').asc())
    return render(request, 'search.html', {'words': words})
