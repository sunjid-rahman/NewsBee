from django.shortcuts import render,get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect,HttpResponse
import requests
import json
from django.urls import reverse
from accounts.models import User
from .models import SharedNews
from .forms import SharedNewsForm
class UserSharedNewsView(generic.ListView,LoginRequiredMixin):
    template_name = 'news/usersharednews.html'
    model=SharedNews
    context_object_name = 'shared_news'
    # queryset=SharedNews.objects.all()
    def get_queryset(self, **kwargs):
        userid=self.request.user
        new_data=SharedNews.objects.filter(shared_by=userid).order_by('-shared_date')
        return new_data
class SharedNewsView(generic.ListView,LoginRequiredMixin):
    template_name = 'news/sharednewslist.html'
    model=SharedNews
    context_object_name = 'shared_news'
    def get_queryset(self, **kwargs):
        userid=self.request.user
        new_data=SharedNews.objects.exclude(shared_by=userid).order_by('-shared_date')
        return new_data
class NewsDataView(generic.TemplateView,LoginRequiredMixin):
    template_name = 'news/newsdata.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search = self.request.GET.get('search', None)
        userid=self.request.user.id
        countryname=User.objects.get(pk=userid).country
        BASE_URL="http://api.mediastack.com/v1/"
        ENDPOINT="news?access_key=1f840598e15ce69ce8a5bdbb72288c6f&languages=en&countries="
        newsUrl=BASE_URL+ENDPOINT+str('us').lower()
        response = requests.get(newsUrl)
        news_data= json.loads(response.content.decode('utf-8'))
        new_data=news_data['data']
        context['newsdata']=new_data
        return context
class SearchNewsDataView(generic.TemplateView,LoginRequiredMixin):
    template_name = 'news/searchnewsdata.html'
    success_url='news/searchnewsdata.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search = self.request.GET.get('search')
        userid=self.request.user.id
        countryname=User.objects.get(pk=userid).country
        BASE_URL="http://api.mediastack.com/v1/news?"
        ENDPOINT="access_key=1f840598e15ce69ce8a5bdbb72288c6f"
        search_key="&keywords="
        lang="&languages=en"
        country="&countries="
        newsUrl=BASE_URL+ENDPOINT+search_key+str(search)+lang+country+"us"
        response = requests.get(newsUrl)
        news_data= json.loads(response.content.decode('utf-8'))
        new_data=news_data['data']
        context['newsdata']=new_data
        context['search']=search
        if not new_data:
            context['status']="empty"
        return context
class SaveSharedNews(LoginRequiredMixin,generic.FormView):
    # fields=('title','author','source','shared_by','created_at','shared_views','description')
    form_class=SharedNewsForm
    success_url=reverse_lazy('news:countrynews')
    template_name = 'news/newsdata.html'
    def form_valid(self,form):
        print(form.errors)
        self.object=form.save(commit=False)
        self.object.save()
        return super().form_valid(form)
class SaveSharedNews1(LoginRequiredMixin,generic.FormView):
    # fields=('title','author','source','shared_by','created_at','shared_views','description')
    form_class=SharedNewsForm
    success_url=reverse_lazy('news:shared_news')
    template_name = 'news/sharednewslist.html'
    def form_valid(self,form):
        print(form.errors)
        self.object=form.save(commit=False)
        self.object.save()
        return super().form_valid(form)
class SaveSharedNews2(LoginRequiredMixin,generic.FormView):
    # fields=('title','author','source','shared_by','created_at','shared_views','description')
    form_class=SharedNewsForm
    success_url=reverse_lazy('news:user_shared_news')
    template_name = 'news/usersharednews.html'
    def form_valid(self,form):
        self.object=form.save(commit=False)
        self.object.save()
        return super().form_valid(form)

class UserSearchNewsDataView(generic.ListView,LoginRequiredMixin):
    template_name = 'news/user_searched.html'
    model=SharedNews
    success_url='news/user_searched.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search = self.request.GET.get('search')
        userid=self.request.user.id
        new_data= SharedNews.objects.filter(title__icontains=search)|SharedNews.objects.filter(author__icontains=search)|SharedNews.objects.filter(description__icontains=search)|SharedNews.objects.filter(category__icontains=search)|SharedNews.objects.filter(source__icontains=search)
        context['newsdata']=new_data
        context['search']=search
        if not new_data:
            context['status']="empty"
        return context
@login_required
def deleteNews(request, pk=None):
    news= get_object_or_404(SharedNews, pk=request.POST.get('pk'))
    creator= news.shared_by
    print(pk)
    print(request.POST.get('pk'))
    print(news.title)
    if request.method == "POST" and request.user.is_authenticated and request.user.id== creator.id:
        news.delete()
        return HttpResponseRedirect(reverse('news:user_shared_news'))


    return HttpResponseRedirect(reverse('news:countrynews'))

# #@login_required
# def SaveSharedNews(request):
#     saved=False
#     if request.method=="POST":
#         print("Hello Post")
#         data=request.POST
#         shared_form = SharedNewsForm(data=data)
#         print(data.keys())
#         if shared_form.is_valid():
#             form=shared_form.save(commit=False)
#             form.save()
#             return HttpResponseRedirect(reverse('news:countrynews'))
#     return HttpResponseRedirect(reverse('news:countrynews'))
