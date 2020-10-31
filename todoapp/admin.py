from django.contrib import admin
from .models import To_Do


# Register your models here.

class ToDoAdmin(admin.ModelAdmin):
    fields = ('description', 'done', 'time_creation')
    list_display = ('id', 'description', 'time_creation', 'done')
    list_filter = ('done', 'time_creation',)
    search_fields = ('id', 'description', 'time_creation')
    save_as = True

admin.site.register(To_Do, ToDoAdmin)