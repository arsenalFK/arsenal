from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class News(models.Model):
    class Meta:
        ordering = ['news_date']
    news_title = models.CharField(max_length=255, verbose_name='Заголовок')
    news_text = models.TextField(verbose_name='Текст')
    news_date = models.DateTimeField(auto_now_add=True)
    news_likes = models.IntegerField(default=0)
    news_image = models.ImageField(null=True, blank=True, verbose_name='Добавить изображение')

    def __str__(self):
        return self.news_title

class Player(models.Model):

    TYPE_GOALKEEPER = 'Вратарь'
    TYPE_DEFENDER = 'Защитник'
    TYPE_MIDFIELDER_DEF = 'Полузащита'
    TYPE_MIDFIELDER_ATK = 'Полунападение'
    TYPE_FORWARD = 'Нападающий'
    TYPE_CHANGE = 'Замена'
    TYPE_CHOICES = (
        (TYPE_GOALKEEPER, 'Вратарь'),
        (TYPE_DEFENDER, 'Защитник'),
        (TYPE_MIDFIELDER_ATK, 'Полунападающий'),
        (TYPE_MIDFIELDER_DEF, 'Полузащитник'),
        (TYPE_FORWARD, 'Нападающий'),
        (TYPE_CHANGE, 'На замене'),
    )

    player_image = models.ImageField(null=True, blank=True, help_text='Фото', verbose_name='Добавить фото')
    player_img = models.ImageField(null=True)
    player_name = models.CharField(max_length=255, help_text='Имя игрока', verbose_name='Имя игрока')
    player_sur_name = models.CharField(max_length=255, help_text='Фамилия игрока', verbose_name='Фамилия игрока')
    birth = models.DateField(null=True)
    player_age = models.SmallIntegerField(help_text='Возраст', verbose_name='Возраст')
    player_compose = models.ForeignKey('Compose', on_delete=models.CASCADE, default=1, help_text='Состав (I/II)', verbose_name='Состав')
    player_position = models.CharField(max_length=13, choices=TYPE_CHOICES, default=TYPE_CHANGE, help_text='Позиция', verbose_name='Игровая позиция')
    weight = models.SmallIntegerField(default=0, null=True)
    height = models.SmallIntegerField(default=0, null=True)
    yellow = models.SmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(99)], verbose_name='Желтые карточки',
                                         help_text='Показатель голкипера (мин - 1, макс - 99)')
    red = models.SmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(99)], verbose_name='Красные карточки',
                                          help_text='Показатель нападения (мин - 1, макс - 99)')
    missed = models.SmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(99)], verbose_name='Пропущено матчей',
                                          help_text='Показатель полузащиты (мин - 1, макс - 99)')
    goals = models.SmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(99)], verbose_name='Забито голов',
                                          help_text='Показатель защиты (мин - 1, макс - 99)')
    def __str__(self):
        return self.player_sur_name

class Compose(models.Model):

    TYPE_I = 1
    TYPE_II = 2
    TYPE_CHOICES = (
        (TYPE_I, 'Первый состав'),
        (TYPE_II, 'Второй состав'),
    )

    compose_name = models.CharField(max_length=255)
    compose = models.PositiveSmallIntegerField(choices=TYPE_CHOICES, default=TYPE_I)

    def __str__(self):
        return self.compose_name

class PlayerRequest(models.Model):

    player_request_name = models.CharField(max_length=255, verbose_name='Имя')
    player_request_name2 = models.CharField(max_length=255, verbose_name='Фамилия')
    player_request_age = models.SmallIntegerField(default=0, verbose_name='Возраст')
    player_request_contacts = models.TextField(verbose_name='Контакты', help_text='Ном.Тел, Viber, WhatsApp, Skype')

    def __str__(self):
        return self.player_request_name2