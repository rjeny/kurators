from django.db import models
from django.contrib.auth.models import User
import uuid

FACULTIES = (
    ('ФФ', 'ФФ'),
    ('ХТА', 'ХТА'),
    ('БТ', 'БТ'),
    ('ХТП', 'ХТП'),
)

# Create your models here.
class Curator (models.Model):
    """Куратор классный парень """
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    photo = models.URLField('Фотография')
    groupName = models.CharField('Группа', max_length=32)
    vk = models.URLField('Идентификатор вк', max_length=64)
    telegram = models.CharField('Идентификтор telegram', max_length=64)
    phone = models.CharField('Телефон', max_length=12)
    public_fields = models.TextField('Доступные поля')

    def __str__(self):
        return self.user.last_name + ' ' + self.user.first_name

    @property
    def full_name(self):
        "Возвращает полное имя"
        return '%s %s' % (self.user.first_name, self.user.last_name)

    class Meta:
        ordering = ["user"]
        verbose_name_plural = "Кураторы"
        verbose_name = "Куратор"


class StudentGroup (models.Model):
    """Группа"""
    id = models.UUIDField('Идентификтор', primary_key=True, default=uuid.uuid4, editable=False)
    faculty = models.CharField('Факультет', choices=FACULTIES, max_length=7)
    number = models.IntegerField('Номер группы')
    curator = models.ForeignKey(Curator, on_delete=models.CASCADE)


class Student (models.Model):
    """Студент"""
    id = models.UUIDField('Идентификтор', primary_key=True, default=uuid.uuid4, editable=False)
    last_name = models.CharField('Фамилия', max_length=128, blank=True)
    first_name = models.CharField('Имя', max_length=128, blank=True)
    phone = models.CharField('Телефон', max_length=11, blank=True)
    group = models.ForeignKey(StudentGroup, on_delete=models.CASCADE)


class CurTime (models.Model):
    """Кураторский час"""
    id = models.UUIDField('Идентификтор', primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField('Название', max_length=256)
    order = models.IntegerField('Порядок')
    desc = models.TextField('Описание')
    manual = models.TextField('Инструкция')
    available = models.BooleanField('Доступность')
    from_to = models.DurationField('Срок')
    stat_factor = models.FloatField('Коэффициент кураторского часа')


class CurTimeResult (models.Model):
    cur_time = models.ForeignKey(CurTime, on_delete=models.CASCADE)
    group = models.ForeignKey(StudentGroup, on_delete=models.CASCADE)
    date = models.DateField('дата проведения')
    problems = models.TextField('Проблемы')
    plus = models.TextField('Плюсы')
    emotions = models.TextField('Эмоции')
    comments = models.TextField('Комментарии')
    cur_rating = models.TextField('Рейтинг кч')
    group_rating = models.TextField('Рейтинг внутригруппового настроя')


class Notification (models.Model):
    """Типы объектов"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    msg = models.TextField('Сообщение')
    object_type = models.IntegerField('Тип объкта')