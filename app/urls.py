from django.conf.urls import url, patterns

from . import views
from .views import AlbumDetailView, MemberDetailView

from django.views.generic import View

from .models import Album

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^albums/$', views.album_list, name='albums'),
    url(r'^albums/(?P<slug>[-\w]+)/$', AlbumDetailView.as_view(), name='album_detail'),
    url(r'^members/$',views.member_list, name='members'),
    url(r'^members/(?P<slug>[-\w]+)/$', MemberDetailView.as_view(), name='member_detail'),
]
