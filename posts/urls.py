from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'posts'

urlpatterns = [
    path('',views.PostList.as_view(),name='all'),
    path('new/',views.CreatePost.as_view(),name = 'create'),
    url(r'by/(?P<username>[-\w]+)',views.Userposts.as_view(),name='for_user'),
    url(r'by/(?P<username>[-\w]+)/(?P<pk>\d)/$',views.PostDetail.as_view(),name='single'),
    url(r'delete/(?P<pk>\d)/$',views.DeletePost.as_view(),name='delete'),

]
