from django.db.models import Count
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from users.models import Subscription
from courses.models import Group


@receiver(post_save, sender=Subscription)
def post_save_subscription(sender, instance: Subscription, created, **kwargs):
    """
    Распределение нового студента в группу курса.

    """
    if created:
        print(f'Новая подписка создана для пользователя {instance.user.username} на курс {instance.course.title}.')

        available_group = Group.objects.filter(course=instance.course).annotate(
            student_count=Count('students')
        ).order_by('student_count').first()

        if available_group and available_group.student_count < 30:
            available_group.students.add(instance.user)
            print(f'Пользователь {instance.user.username} добавлен в группу {available_group.title}.')
        else:
            print(f'Нет доступной группы для курса {instance.course.title}.')
    else:
        print(f'Подписка {instance.id} обновлена.')
