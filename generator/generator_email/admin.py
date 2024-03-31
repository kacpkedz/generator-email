from django.contrib import admin
from .models import Employee

@admin.register(Employee)  # Dekorator rejestrujący model Employee w panelu admina Django
class EmployeeAdmin(admin.ModelAdmin):  # Definicja klasy EmployeeAdmin dziedziczącej po admin.ModelAdmin
    list_display = ('first_name', 'last_name', 'email')  # Lista pól wyświetlanych w panelu admina
    search_fields = ('first_name', 'last_name', 'email')  # Pola, po których można wyszukiwać rekordy w panelu admina
