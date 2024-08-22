from django.contrib import admin
from .models import CustomUser, Balance, Subscription

admin.site.register(CustomUser)
admin.site.register(Subscription)

@admin.register(Balance)
class BalanceAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount')
    search_fields = ('user__email',)
