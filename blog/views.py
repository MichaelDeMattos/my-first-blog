from django.shortcuts import render
from .models import Post
from django.utils import timezone


# Create your views here.

# cria uma função que vai fazer uma requisição e renderizar nossa pagina main
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now())
    return render(request, 'blog/post_list.html',
                  {'posts': posts})


def sobre_dev(request):
    return render(request, 'blog/sobre.html',
                  {})


