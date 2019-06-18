from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'groups'

urlpatterns = [
    path('',views.ListGroupe.as_view(),name = 'Group_list'),
    path('new',views.CreateGroupeView.as_view(),name = 'create'),
    url(r'^posts/in/(?P<slug>[-\w]+)/$',views.singleGroupe.as_view(),name = 'single'),
]
