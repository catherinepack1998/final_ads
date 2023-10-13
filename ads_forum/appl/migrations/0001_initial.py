# Generated by Django 4.2.6 on 2023-10-13 00:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ads',
            fields=[
                ('ad_id', models.BigAutoField(primary_key=True, serialize=False, unique=True)),
                ('heading', models.CharField(max_length=128, verbose_name='Заголовок')),
                ('content', models.FileField(blank=True, upload_to='content/%Y/%m/%d/', verbose_name='Загрузить файл')),
                ('text', models.TextField(verbose_name='Текст')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('category', models.CharField(choices=[('TT', 'Танк'), ('HIL', 'Хил'), ('DD', 'ДД'), ('TRADER', 'Торговец'), ('GILDMASTER', 'Гильдмастер'), ('QUESTGIVER', 'Квестгивер'), ('FARRIER', 'Кузнец'), ('TANNER', 'Кожевник'), ('CHEMIST', 'Зельевар'), ('WIZARD', 'Мастер заклинаний')], default='DD', max_length=50, verbose_name='Категория')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AdResponses',
            fields=[
                ('response_id', models.BigAutoField(primary_key=True, serialize=False, unique=True)),
                ('response_text', models.TextField(blank=True, max_length=255, verbose_name='Текст отклика')),
                ('ad_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appl.ads', verbose_name='Объявление')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
    ]