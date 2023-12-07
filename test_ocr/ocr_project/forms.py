from django.db import models
from django.forms import fields
from .models import ImageUploadedForm
from django import forms

# class UserImageForm(forms.ModelForm):
#     class meta:
#         models = UploadImage
#         fields = '__all__'

# class UploadFileForm(forms.Form):
#     title = forms.CharField(max_length=50)
#     file = forms.ImageField()

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageUploadedForm
        fields = ['image']