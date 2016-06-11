from django.contrib import admin
from .forms import MultipleModelAlbum, MultipleModelTeam
from .models import Member, Team, Album

#Class for formField
class TeamAdmin(admin.ModelAdmin):
    form = MultipleModelTeam

class AlbumAdmin(admin.ModelAdmin):
    form = MultipleModelAlbum
    prepopulated_fields = {'slug':('album_name',)}

class MemberAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('member_name',)}
# Register your models here.
admin.site.register(Member, MemberAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Album, AlbumAdmin)
