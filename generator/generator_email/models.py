from django.db import models
from django.core.validators import EmailValidator
from django.utils.translation import gettext_lazy as _

class Employee(models.Model):
    first_name = models.CharField(_('first name'), max_length=100)  # Pole przechowujące imię pracownika
    last_name = models.CharField(_('last name'), max_length=100)  # Pole przechowujące nazwisko pracownika
    email = models.EmailField(_('email address'), unique=True)  # Pole przechowujące adres e-mail pracownika, unikalne

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"  # Metoda zwracająca czytelny opis pracownika

    def save(self, *args, **kwargs):
        if not self.email:  # Jeśli pole email jest puste
            domain = 'nasza_firma.com'  # Domena e-mail
            email = f"{self.first_name.lower()}.{self.last_name.lower()}@{domain}"  # Generowanie adresu e-mail na podstawie imienia i nazwiska
            num = 1
            while Employee.objects.filter(email=email).exists():  # Dopóki istnieje pracownik o takim samym adresie e-mail
                email = f"{self.first_name.lower()}.{self.last_name.lower()}{num}@{domain}"  # Dodanie numeru przedrostka w razie konfliktu
                num += 1
            self.email = email  # Przypisanie wygenerowanego adresu e-mail do pola email
        super().save(*args, **kwargs)  # Wywołanie metody save() z klasy nadrzędnej, aby zapisać obiekt w bazie danych

