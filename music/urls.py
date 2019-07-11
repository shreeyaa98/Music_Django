from django.conf.urls import url
from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    url(r'^$',views.index,name='index'),#index is a variable which refrences this url pattern
    #/music/album_id/ saves the no. being passed as album_id
    url(r'^(?P<album_id>[0-9]+)/$',views.detail,name='detail'),
     #/music/album_id/favorite perform some logic and render the same page
    url(r'^(?P<album_id>[0-9]+)/favorite/$',views.favorite,name='favorite')
]
