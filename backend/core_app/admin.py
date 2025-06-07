from django.contrib import admin

# Register your models here.
from backend.core_app.models import Transactions, Budget, Pots

@admin.register(Transactions)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'amount', 'is_recurring', 'user')
    search_fields = ('name', 'type')
    list_filter = ('type', 'is_recurring', 'user')
    ordering = ('-id',)


@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    list_display = ('category', 'maximum', 'theme')
    search_fields = ('category',)
    list_filter = ('category', 'theme')
    ordering = ('-id',)


@admin.register(Pots)
class PotAdmin(admin.ModelAdmin):
    list_display = ('name', 'target', 'total', 'theme', 'user')
    search_fields = ('name',)
    list_filter = ('theme', 'user')
    ordering = ('-id',)
