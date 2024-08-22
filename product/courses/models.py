from django.db import models
from django.utils import timezone

class Course(models.Model):
    """Модель продукта - курса."""
    author = models.CharField(
        max_length=250,
        verbose_name='Автор',
    )
    title = models.CharField(
        max_length=250,
        verbose_name='Название',
    )
    start_date = models.DateTimeField(
        auto_now=False,
        auto_now_add=False,
        verbose_name='Дата и время начала курса'
    )
    price = models.DecimalField(
        max_digits = 10,
        decimal_places = 2,
        verbose_name = 'Стоимость'
    )

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        ordering = ('-id',)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.price < 0:
            raise ValidationError(_('Стоимость не может быть отрицательным.'))
        super().save(*args, **kwargs)


class Lesson(models.Model):
    """Модель урока."""
    course = models.ForeignKey(
        'courses.Course',
        on_delete=models.CASCADE,
        related_name = 'lessons',
        verbose_name = 'Курс',
        # null=True,
        # blank=True
    )

    title = models.CharField(
        max_length=250,
        verbose_name='Название',
    )
    link = models.URLField(
        max_length=250,
        verbose_name='Ссылка',
    )

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
        ordering = ('id',)

    def __str__(self):
        return f'{self.course.title} - {self.title}'


class Group(models.Model):
    """Модель группы."""

    course = models.ForeignKey(
        Course,
        related_name='groups',
        on_delete=models.CASCADE,
        verbose_name='Курс',
        # null=True,
        # blank=True
    )

    title = models.CharField(
        max_length=100,
        verbose_name='Название группы'
    )

    students = models.ManyToManyField(
        'users.CustomUser',
        related_name='group',
        verbose_name='Студенты',
    )

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
        ordering = ('-id',)

    def __str__(self):
        return f'{self.course.title} - {self.title}'

