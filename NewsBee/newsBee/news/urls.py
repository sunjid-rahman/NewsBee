from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
app_name="news"
urlpatterns=[
    path('countrynews/',views.NewsDataView.as_view(),name='countrynews'),
    path('saveSharedNews/',views.SaveSharedNews.as_view(),name='create_news'),
    path('sharednews/',views.SharedNewsView.as_view(),name='shared_news'),
    path('search_news/',views.SearchNewsDataView.as_view(),name='search_news'),
    path('user_search_news/',views.UserSearchNewsDataView.as_view(),name='user_search_news'),
    path('user_shared_news/',views.UserSharedNewsView.as_view(),name='user_shared_news'),
    path('saveSharedNewsfromUser/',views.SaveSharedNews1.as_view(),name='create1_news'),
    path('saveSharedNewsfromMe/',views.SaveSharedNews2.as_view(),name='create2_news'),
    path('delete/<int:pk>/',views.deleteNews,name='delete'),
]
