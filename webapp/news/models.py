from django.db import models
from django import forms


class Articles(models.Model):
    '''данные о посте '''
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Aнонс', max_length=250)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Comments(models.Model):
    """Комментарии"""
    email = models.EmailField()
    name = models.CharField('Имя пользователя', max_length=50)
    text_comments = models.TextField('Текст комментария', max_length=2000)
    post = models.ForeignKey(Articles, verbose_name='Публикации', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} , {self.post}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class Likes(models.Model):
    ip = models.CharField('IP-адрес', max_length=100)
    pos = models.ForeignKey(Articles, verbose_name='Публикация', on_delete=models.CASCADE)


