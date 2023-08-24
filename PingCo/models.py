from django.db import models


class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Subscriber'
        verbose_name_plural = 'Subscribers'

    def __str__(self):
        return f'Mail: {self.email}'
