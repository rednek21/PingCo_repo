from django.db.models import Count
from django.shortcuts import render

from PingCo.models import Subscriber
from blog.models import Category, Post, Tag
from common.tasks import sub_email, self_email
from PingCo.forms import NewsletterSubForm, FeedbackForm


class CommonContextMixin:
    title = None

    def get_context_data(self, **kwargs):
        context = super(CommonContextMixin, self).get_context_data(**kwargs)
        context['title'] = self.title
        return context


class BlogContextMixin:

    def get_context_data(self, **kwargs):
        context = super(BlogContextMixin, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['similar_posts'] = Post.objects.all().order_by('?')[:5]
        context['popular_tags'] = Tag.objects.annotate(num_posts=Count('tags')).order_by('-num_posts')[:8]
        return context


class CommonFormsMixin:
    template_name = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sf'] = NewsletterSubForm()
        context['ff'] = FeedbackForm()
        return context

    def post(self, request, *args, **kwargs):
        sub_form = NewsletterSubForm(request.POST)
        feedback_form = FeedbackForm(request.POST)

        if sub_form.is_valid():
            email = sub_form.cleaned_data['email']
            if Subscriber.objects.filter(email=email).exists():
                sub_email(email, True)
            else:
                new_sub = Subscriber(email=email)
                sub_email(email, False)
                new_sub.save()

        if feedback_form.is_valid():
            name = feedback_form.cleaned_data['name']
            email = feedback_form.cleaned_data['email_']
            phone = feedback_form.cleaned_data['phone']
            message = f'Отправитель: {name} \nEmail: {email} \nPhone: {phone} \n'
            self_email('FeedbackForm', message)

        context = self.get_context_data(**kwargs)
        context['sf'] = sub_form
        context['ff'] = feedback_form

        return render(request, self.template_name, context)
