from django.shortcuts import render, redirect
from .models import Articles, Likes
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView
from django.views.generic.base import View
from .forms import CommentsForm
from django.views.generic import ListView


def news_home(request):
    """ Вывод записей """
    news = Articles.objects.order_by('date')
    return render(request, 'news/news_home.html', {'news': news})


class NewsDetailView(DetailView):
    """ Отдельная страница записи"""
    model = Articles
    template_name = 'news/details_views.html'
    context_object_name = 'article'


class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/news-update.html'

    form_class = ArticlesForm


class NewsDeleteView(DeleteView):
    model = Articles
    success_url = '/news/'
    template_name = 'news/news-delete.html'


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Форма была неверной'

    form = ArticlesForm()
    date = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', date)


class AddComments(View):
    """Добавление комментария"""

    def post(self, request, pk):
        form = CommentsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post_id = pk
            form.save()
        return redirect(f'/news/{pk}')


class Search(ListView):
    """Поиск"""
    template_name = 'news/news_home.html'
    context_object_name = 'news'
    paginate_by = 5

    def get_queryset(self):
        return Articles.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self,  *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q', '')
        return context


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class AddLike(View):
    def get(self, request, pk):
        ip_client = get_client_ip(request)
        try:
            Likes.objects.get(ip=ip_client, pos_id=pk)
            return redirect(f'/news/{pk}')
        except:
            new_like = Likes()
            new_like.ip = ip_client
            new_like.pos_id = int(pk)
            new_like.save()
            return redirect(f'/news/{pk}')


class DelLike(View):
    def get(self, request, pk):
        ip_client = get_client_ip(request)
        try:
            lik = Likes.objects.get(ip=ip_client)
            lik.delete()
            return redirect(f'/news/{pk}')
        except:
            return redirect(f'/news/{pk}')






