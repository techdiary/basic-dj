from django import forms

from .models import Member, Album, Team

class MultipleModelAlbum(forms.ModelForm):
    members = forms.ModelMultipleChoiceField(queryset=Member.objects.all(),widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Album
        fields = ['album_name','slug','members','album_pub_date']


class MultipleModelTeam(forms.ModelForm):
    members = forms.ModelMultipleChoiceField(queryset=Member.objects.all(),widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Team
        fields = ['team_name','members','events','events_pub_date']
