from django.db import models


class Poll(models.Model):
    question = models.TextField(max_length=2000, verbose_name='Опрос')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f'{self.pk}. {self.created_at}: {self.question}'

    class Meta:
        db_table = 'polls'
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'


class Choice(models.Model):
    option_text = models.TextField(max_length=2000, verbose_name='Текст Варианта')
    poll = models.ForeignKey('webapp.Poll', on_delete=models.CASCADE, related_name='choices', verbose_name='Опросы')

    def __str__(self):
        return f'{self.pk}. {self.option_text}: {self.poll}'

    class Meta:
        db_table = 'choices'
        verbose_name = 'Вариант'
        verbose_name_plural = 'Варианты'
