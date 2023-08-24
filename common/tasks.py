from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail


@shared_task
def self_email(form_title, message):
    subject = f'Отправлено с формы {form_title}'
    send_mail(
        subject=subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[settings.EMAIL_HOST_USER],
        fail_silently=False,
    )


@shared_task
def sub_email(email, error=None):
    if error:
        message = 'Вы уже подписаны на рассылку от PingCo!'
    else:
        message = 'Благодарим за подписку на нашу рассылку! Вы не пожалеете'

    subject = f'Подписка на рассылку от PingCo'

    send_mail(
        subject=subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email],
        fail_silently=False,
    )

    if error is None or error == False:
        message = f'Пользователь {email} подписался на рассылку'
        self_email('SubscribeForm', message)
