from django import forms
from django.contrib import admin
from .models import SharedNews
class SharedNewsForm(forms.ModelForm):
    class Meta:
        fields=('title','author','source','shared_by','created_at','shared_views','category','image','description')
        model=SharedNews
