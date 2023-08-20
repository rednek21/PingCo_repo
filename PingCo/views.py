from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from common.views import CommonContextMixin, CommonFormsMixin
from .forms import ContactForm

from .tasks import self_email


# def is_ajax(request):
#     return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


class IndexView(CommonContextMixin, CommonFormsMixin, TemplateView):  # sub, feedback
    # template_name = 'PingCo/index.html'
    template = 'PingCo/index.html'
    title = 'IT-компания PingCo'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['index'] = 'current-item'
        context['index_view'] = 'index'
        return context


class BlogView(CommonContextMixin, CommonFormsMixin, TemplateView):  # feedback
    # template_name = 'PingCo/blog.html'
    template = 'PingCo/blog.html'
    title = 'PingCo - Блог'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog'] = 'current-item'
        return context


class AboutView(CommonContextMixin, CommonFormsMixin, TemplateView):  # sub, feedback
    # template_name = 'PingCo/about.html'
    template = 'PingCo/about.html'
    title = 'PingCo - О нас'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = 'current-item'
        context['about_view'] = 'about'
        return context


class MissionView(CommonContextMixin, CommonFormsMixin, TemplateView):  # sub, feedback
    # template_name = 'PingCo/vision-mission.html'
    template = 'PingCo/vision-mission.html'
    title = 'PingCo - Наша миссия'

    # def get_success_url(self):
    #     return reverse_lazy('PingCo:mission')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_visions'] = 'page-visions'
        context['about'] = 'current-item'
        context['mission_view'] = 'mission'
        return context


class TeamView(CommonContextMixin, CommonFormsMixin, TemplateView):  # sub, feedback
    # template_name = 'PingCo/team.html'
    template = 'PingCo/team.html'
    title = 'PingCo - Команда'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['team'] = 'current-item'
        context['team_view'] = 'team'
        return context

    # def get_success_url(self):
    #     return reverse_lazy('PingCo:team')


class ContactView(CommonContextMixin, CommonFormsMixin, TemplateView):  # sub, feedback, contact
    # template_name = 'PingCo/contact.html'
    template = 'PingCo/contact.html'
    title = 'PingCo - Контакты'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact'] = 'current-item'
        context['contact_view'] = 'contact'
        return context

    def get(self, request, *args, **kwargs):
        contact_form = ContactForm()

        context = self.get_context_data()
        context['cf'] = contact_form

        return render(request, self.template, context)

    def post(self, request, *args, **kwargs):
        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():
            name = contact_form.cleaned_data['name']
            email = contact_form.cleaned_data['email__']
            phone = contact_form.cleaned_data['phone']
            subject = contact_form.cleaned_data['subject']
            message_ = contact_form.cleaned_data['message']

            message = f'Отправитель: {name} \nEmail: {email} \nPhone: {phone} \nSubject: {subject} \nMessage: {message_}'
            subject_ = f'Заявка с формы Contacts'

            self_email(subject_, message)

        context = self.get_context_data()
        context['cf'] = contact_form

        return render(request, self.template, context)

    def get_success_url(self):
        return reverse_lazy('PingCo:contact')


class RoadMapView(CommonContextMixin, CommonFormsMixin, TemplateView):  # sub, feedback
    # template_name = 'PingCo/roadmap.html'
    template = 'PingCo/roadmap.html'
    title = 'PingCo - Дизайн'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['case'] = 'current-item'
        context['roadmap_view'] = 'roadmap'
        return context


class AssetView(CommonContextMixin, CommonFormsMixin, TemplateView):  # sub, feedback
    # template_name = 'PingCo/parti-asset.html'
    template = 'PingCo/parti-asset.html'
    title = 'PingCo - Разработка сайтов'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['case'] = 'current-item'
        context['asset_view'] = 'parti_assets'
        return context


class BlogDetailView(CommonContextMixin, CommonFormsMixin, TemplateView):  # sub, feedback
    # template_name = 'PingCo/blog-details.html'
    template = 'PingCo/blog-details.html'
    title = 'PingCo - Blog-details'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog_detail'] = 'current-item'
        context['blog_detail_view'] = 'blog_details'
        return context
