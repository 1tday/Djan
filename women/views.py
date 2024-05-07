from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify

from women.models import Women

menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title':'Добавить статью', 'url_name': 'add_page'},
        {'title':'Обратная связь', 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'},
]

data_db =[
    {'id': 1, 'title': "Анделина Джоли", 'content': 'Биография Анджелины Джоли', 'is_published': True},
    {'id': 2, 'title': "Марго Робби", 'content': 'Биография Марго Робби', 'is_published': False},
    {'id': 3, 'title': "Джулия Робертс", 'content': 'Биография Джулия Робертс', 'is_published': True},
]

cats_db = [
    {'id': 1, 'name': 'Актрисы'},
    {'id': 2, 'name': 'Певицы'},
    {'id': 3, 'name': 'Спортсменки'},
]

def index(request): #HttpRequest
    posts = Women.published.all()
    data = {'title': 'Главная страница',
            'menu': menu,
            'posts': posts,
            'cat_selected': 0,
            }
    #t = render_to_string('women/index.html')
    #return HttpResponse(t)
    return render(request, 'women/index.html', context=data)

def about(request):
    data = {'title': 'О сайте', 'menu': menu}
    return render(request, 'women/about.html', context=data)


def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)

    data = {'title': post.title,
            'menu': menu,
            'post': post,
            'cat_selected': 1,
    }
    return render(request, 'women/post.html', data)
def addpage(request):
    return HttpResponse(f"Добавление статьи")


def contact(request):
    return HttpResponse(f"Обратная связь")


def login(request):
    return HttpResponse(f"Авторизация")

def show_category(request, cat_id):
    data = {
        'title': 'Отображение по рубрикам',
        'menu': menu,
        'posts': data_db,
        'cat_selected': cat_id,
    }
    return render(request, 'women/index.html', context=data)


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")

'''def categories(request, cat_id): #HttpRequest
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
'''
