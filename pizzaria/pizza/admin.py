from django.contrib import admin

from .models import Pizza


class PizzaAdmin(admin.ModelAdmin):
    search_fields = ['name', 'ingredients']
    list_display = ['name', 'ingredients']


admin.site.register(Pizza, PizzaAdmin)
