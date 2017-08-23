from django.db import models
import uuid


# Create your models here.
class Curator (models.Model):
    """Куратор классный парень """
    id = models.UUIDField('Идентификтор', primary_key=True, default=uuid.uuid4, editable=False)
    second_name = models.CharField('Фамилия', max_length=128)
    first_name = models.CharField('Имя', max_length=128)
    middle_name = models.CharField('Отчество', max_length=128)
    photo = models.URLField('Фотография')
    groupName = models.CharField('Группа', max_length=32)
    vk = models.URLField('Идентификатор вк', max_length=64)
    telegram = models.CharField('Идентификтор telegram', max_length=64)
    email = models.EmailField('Email')
    password = models.CharField('Пароль', max_length=128)
    public_fields = models.TextField('Доступные поля')


class Group (models.Model):
    """Группа"""
    id = models.UUIDField('Идентификтор', primary_key=True, default=uuid.uuid4, editable=False)
    prefix = models.CharField('Префикс', max_length=8)
    number = models.IntegerField('Номер группы')
    curator = models.ForeignKey(Curator, on_delete=models.CASCADE)


class Student (models.Model):
    """Студент"""
    id = models.UUIDField('Идентификтор', primary_key=True, default=uuid.uuid4, editable=False)
    second_name = models.CharField('Фамилия', max_length=128)
    first_name = models.CharField('Имя', max_length=128)


class CurTime (models.Model):
    """Кураторский час"""
    id = models.UUIDField('Идентификтор', primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField('Фамилия', max_length=256)
    order = models.IntegerField('Фамилия')
    desc = models.TextField('Описание')
    manual = models.TextField('Инструкция')
    available = models.BooleanField('Доступность')
    from_to = models.DurationField('Срок')
    stat_factor = models.FloatField('Коэффициент кураторского часа')


class CurTimeResult (models.Model):
    cur_time = models.ForeignKey(CurTime, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date = models.DateField('дата проведения')
    cur_rating = models.CharField('Рейтинг кч', max_length=255)
    group_rating = models.CharField('Рейтинг внутригруппового настроя', max_length=255)