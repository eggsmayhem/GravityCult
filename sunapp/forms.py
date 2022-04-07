from django import forms
from sunapp.models import Image
class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Image
        fields = ('title', 'author','image', 'location', 'content')