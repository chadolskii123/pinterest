from django.forms import ModelForm

from projectapp.models import Project


class ProejctCreationForm(ModelForm):
    class Meta:
        model = Project
        fields = ['image', 'title', 'description']
