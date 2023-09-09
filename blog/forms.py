from django import forms

from blog.models import Post


class SearchbarForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'text', 'placeholder': 'Искать по названиям...',
    }), required=False)

    class Meta:
        model = Post
        fields = ('title',)
