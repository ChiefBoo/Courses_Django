# Generated by Django 4.2.10 on 2024-08-21 14:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_lesson_course_alter_course_start_date'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='balance',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=1000, max_digits=10, verbose_name='Сумма'),
        ),
        migrations.AddField(
            model_name='balance',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='balance', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='subscription',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to='courses.course'),
        ),
        migrations.AddField(
            model_name='subscription',
            name='subscribed_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата подписки'),
        ),
        migrations.AddField(
            model_name='subscription',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to=settings.AUTH_USER_MODEL),
        ),
    ]
