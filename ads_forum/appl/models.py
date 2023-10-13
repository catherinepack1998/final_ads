from django.db import models
from django.contrib.auth.models import User

class Ads(models.Model):
    ad_id = models.BigAutoField(primary_key=True, unique=True)
    heading = models.CharField(max_length=128, verbose_name='Заголовок')     
    content = models.FileField(blank=True, upload_to="content/%Y/%m/%d/", verbose_name='Загрузить файл')
    text = models.TextField(verbose_name='Текст')
    create_date = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    TANK = 'TT'
    HIL = 'HIL'
    DD = 'DD'
    TRADER = 'TRADER'
    GILDMASTER = 'GILDMASTER'
    QUESTGIVER = 'QUESTGIVER'
    FARRIER = 'FARRIER'
    TANNER = 'TANNER'
    CHEMIST = 'CHEMIST'
    WIZARD = 'WIZARD'
    CATEGORY = [
        (TANK, 'Танк'),
        (HIL, 'Хил'),
        (DD, 'ДД'),
        (TRADER, 'Торговец'),
        (GILDMASTER, 'Гильдмастер'),
        (QUESTGIVER, 'Квестгивер'),
        (FARRIER, 'Кузнец'),
        (TANNER, 'Кожевник'),
        (CHEMIST, 'Зельевар'),
        (WIZARD, 'Мастер заклинаний'),
    ]
    category = models.CharField(
        choices=CATEGORY,
        default=DD,
        max_length=50,
        verbose_name='Категория',
    )
    def __str__(self):
        return self.heading

class AdResponses(models.Model):
    response_id = models.BigAutoField(primary_key=True, unique=True)
    response_text = models.TextField(blank=True, max_length=255, verbose_name='Текст отклика')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    ad_id = models.ForeignKey(Ads, on_delete=models.CASCADE, verbose_name='Объявление')


    def __str__(self):
        return f'{self.response_id}'
     

