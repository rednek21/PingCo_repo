from django import forms

from PingCo.models import Subscriber


class NewsletterSubForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'type': 'email', 'class': 'form-control', 'placeholder': 'Ваш email', 'id': 'email',
    }))

    class Meta:
        model = Subscriber
        fields = ('email',)


class FeedbackForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'text', 'class': 'form-control', 'placeholder': 'Введите имя', 'id': 'name'
    }))
    email_ = forms.EmailField(widget=forms.TextInput(attrs={
        'type': 'email', 'class': 'form-control', 'placeholder': 'Ваш email', 'id': 'email_'
    }))
    phone = forms.IntegerField(widget=forms.TextInput(attrs={
        'type': 'text', 'class': 'form-control', 'placeholder': 'Введите номер телефона', 'id': 'phone'
    }))

    class Meta:
        fields = ('name', 'email_', 'phone',)


class ContactForm(forms.Form):
    CHOICES = (
        ('Работа', 'Работа'),
        ('SEO', 'SEO'),
        ('Дизайн', 'Дизайн'),
    )

    name = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'text', 'class': 'form-control', 'placeholder': 'Введите имя', 'id': 'name'
    }))
    email__ = forms.EmailField(widget=forms.EmailInput(attrs={
        'type': 'email', 'class': 'form-control', 'placeholder': 'Введите почту', 'id': 'email__'
    }))
    phone = forms.IntegerField(widget=forms.TextInput(attrs={
        'type': 'text', 'class': 'form-control', 'placeholder': 'Введите номер телефона', 'id': 'phone'
    }))
    subject = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={
        'id': 'subject', 'class': 'form-control'
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'name': 'mess', 'id': 'mess', 'cols': '30', 'rows': '10', 'placeholder': 'Сообщение'
    }))

    class Meta:
        fields = ('name', 'email__', 'phone', 'subject', 'message',)
