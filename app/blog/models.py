from django.db import models
from django.urls import reverse


class Post(models.Model):
    class Meta:
        verbose_name = 'Статьи'
        verbose_name_plural = 'Статьи'
        ordering = ['time_create']

    title = models.CharField(max_length=255,
                             verbose_name="Заголовок", )
    content = models.TextField(blank=True,
                               verbose_name="Текст", )
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/",
                              verbose_name="Фото", )
    time_create = models.DateTimeField(auto_now_add=True,
                                       verbose_name="Время создания", )
    time_update = models.DateTimeField(auto_now=True,
                                       verbose_name="Время изменения", )
    is_published = models.BooleanField(default=True,
                                       verbose_name="Публикация", )

    CHOICES = (
        ('Человек', 'MAN'),
        ('Техника', 'ELECTRONICS'),
    )

    category = models.CharField(max_length=15,
                                choices=CHOICES, )

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    def __str__(self):
        return self.title
