from django.shortcuts import render


# Create your views here.

# cria uma função que vai fazer uma requisição e renderizar nossa pagina main
def post_list(request):
    return render(request, 'blog/post_list.html',
                  {})
