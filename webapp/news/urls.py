from django.urls import path
from . import views


urlpatterns = [

    path('', views.news_home, name='news_home'),
    path('create', views.create, name='create'),
    path('<int:pk>/', views.NewsDetailView.as_view(), name='news-detail'),
    path('<int:pk>/update', views.NewsUpdateView.as_view(), name='news-update'),
    path('<int:pk>/delete', views.NewsDeleteView.as_view(), name='news-delete'),
    path('review/<int:pk>/', views.AddComments.as_view(), name='add_comments'),
    path('search/', views.Search.as_view(), name='search'),
    path('<int:pk>/add_likes', views.AddLike.as_view(), name='add_likes'),
    path('<int:pk>/del_likes', views.DelLike.as_view(), name='del_likes'),

]