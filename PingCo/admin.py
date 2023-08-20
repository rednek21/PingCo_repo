from django.contrib import admin

from PingCo.models import Subscriber


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    fields = ['email', 'subscribed']
    list_display = ['email']
