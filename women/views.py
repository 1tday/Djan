from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify

menu = ['О сайте', 'Добавить статью', 'Обратная связь', "Войти"]

data_db =[
    {'id': 1, 'title': "Анделина Джоли", 'content': 'Биография Анджелины Джоли', 'is_published': True},
    {'id': 2, 'title': "Марго Робби", 'content': 'Биография Марго Робби', 'is_published': False},
    {'id': 3, 'title': "Джулия Робертс", 'content': 'Биография Джулия Робертс', 'is_published': True},
]

def index(request): #HttpRequest
    data = {'title': 'Главная страница',
            'menu': menu,
            'posts': data_db
            }
    #t = render_to_string('women/index.html')
    #return HttpResponse(t)
    return render(request, 'women/index.html', context=data)

def about(request):
    data = {'title': 'О сайте'}
    return render(request, 'women/about.html', context=data)

def categories(request, cat_id): #HttpRequest
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>id: {cat_id}")
def categories_by_slug(request, cat_slug): #HttpRequest
    print(request.GET)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>slug: {cat_slug}")

def archive(request, year):
    if year > 2023:
        # raise Http404()
        # return redirect('/', permanent=True)
        # return redirect(index)
        # return redirect('home')
        uri = reverse('cats', args=('sport',))
        #return redirect(uri)
        #return HttpResponseRedirect('/')
        return HttpResponsePermanentRedirect(uri)
    return HttpResponse(f"<h1>Архив по годам</h1><p>year: {year}")

def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
