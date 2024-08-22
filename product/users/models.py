from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    """Кастомная модель пользователя - студента."""

    email = models.EmailField(
        verbose_name='Адрес электронной почты',
        max_length=250,
        unique=True
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = (
        'username',
        'first_name',
        'last_name',
        'password'
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('-id',)

    def __str__(self):
        return self.get_full_name()


class Balance(models.Model):
    """Модель баланса пользователя."""

    user = models.OneToOneField(
        'users.CustomUser',
        on_delete= models.CASCADE,
        verbose_name = 'Пользователь',
        # null = True,
        # blank = True
    )

    amount = models.DecimalField(
        max_digits = 10,
        decimal_places = 2,
        default = 1000,
        verbose_name = 'Сумма'
    )

    class Meta:
        verbose_name = 'Баланс'
        verbose_name_plural = 'Балансы'
        ordering = ('-id',)

    def __str__(self):
        return f'{self.user.email} - {self.amount}'

    def save(self, *args, **kwargs):
        if self.amount < 0:
            raise ValidationError(_('Баланс не может быть отрицательным.'))
        super().save(*args, **kwargs)


class Subscription(models.Model):
    """Модель подписки пользователя на курс."""

    user = models.ForeignKey(
        'users.CustomUser',
        on_delete = models.CASCADE,
        related_name = 'subscriptions',
        # null = True,
        # blank = True
    )
    course = models.ForeignKey(
        'courses.Course',
        on_delete = models.CASCADE,
        related_name = 'subscriptions',
        # null=True,
        # blank=True
    )
    subscribed_at = models.DateTimeField(
        auto_now_add = True,
        verbose_name = 'Дата подписки',
        # null=True,
        # blank=True
    )
    is_valid = models.BooleanField(
        verbose_name='Доступ',
        default=False
    )

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        ordering = ('-id',)
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'course'],
                name='subscription_unique'
            ),
        ]

    def __str__(self):
        return f'{self.user.email} - {self.courses.title}'

