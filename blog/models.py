from django.db import models
from django.urls import reverse
from pytils.translit import slugify


class Category(models.Model):
    title = models.CharField(max_length=32, unique=True)
    slug = models.CharField(unique=True, blank=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('blog:post_with_category', kwargs={'category_slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        return super().save(*args, **kwargs)


class Tag(models.Model):
    title = models.CharField(max_length=32, unique=True)
    slug = models.CharField(unique=True, blank=True)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('blog:post_with_tag', kwargs={'tag_slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        return super().save(*args, **kwargs)


class Post(models.Model):
    title = models.CharField(max_length=256, unique=True)
    preview_text = models.TextField()
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, related_name='posts')
    tag = models.ManyToManyField(to=Tag, related_name='tags')
    image = models.ImageField(upload_to='post_images')
    image_text = models.CharField(max_length=128, null=True, blank=True)
    main_text = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)
    slug = models.CharField(unique=True, blank=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('blog:blog_details', kwargs={'post_slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        return super().save(*args, **kwargs)
