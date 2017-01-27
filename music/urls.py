from django.conf.urls import url
from . import views
app_name='music'




urlpatterns = [
    #/music/
    #url(r'^$',views.index,name='index'),

    #/music/someid/
    #^ ->begging
    #$ ->end
    # P ->matching pattern
    # /music/<album_id>/
    #url(r'^(?P<album_id>[0-9]+)/$',views.detail,name='detail'),

    # /music/<album_id>/favorite
    #url(r'^(?P<album_id>[0-9]+)/favorite/$',views.favorite,name='favorite'),

#url(r'^login1/$',views.login1,name='login1'),
url(r'^login1/$', views.login1, name='login1'),
url(r'^$',views.index,name='index'),
url(r'^alll/$',views.alll,name='alll'),
url(r'^display/$',views.display,name='display'),
#url(r'^$',views.IndexView.as_view(),name='index'),
url(r'^register/$',views.UserFormView.as_view(),name='register'),
#url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name='detail'),
#/music/album/add
url(r'album/add/$',views.AlbumCreate.as_view(),name='album-add'),

url(r'^album/(?P<pk>[0-9]+)/$',views.AlbumUpdate.as_view(),name='album-update'),
#url(r'^album/(?P<pk>[0-9]+)/delete/$',views.AlbumDelete.as_view(),name='album-delete'),
url(r'^logout_user/$',views.logout_user,name='logout_user'),
url(r'^post/new/$', views.transport_new, name='post_new'),
url(r'^(?P<album_id>[0-9]+)/delete_album/$', views.delete_album, name='delete_album'),
url(r'^(?P<album_id>[0-9]+)/detail/$', views.detail, name='detail'),
]
