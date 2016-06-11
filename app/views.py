from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone

from .models import Album, Member, Team

from django.views.generic.detail import DetailView
from django.template import context

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at app index")
# MEMBERS
class MemberDetailView(DetailView):
    model = Member

    def get_success_url(self):
        return self.get_object().get_absolute_url()

def member_list(request):
    members_list = Member.objects.all()
    return render(request, 'app/members.html',{'members_list':members_list})

#ALBUM
class AlbumDetailView(DetailView):
        model = Album

        def get_success_url(self):
            return self.get_object().get_absolute_url()

def album_list(request):
    latest_album_list = Album.objects.all()
    context = {'latest_album_list': latest_album_list}
    return render(request,'app/albums.html',context)
