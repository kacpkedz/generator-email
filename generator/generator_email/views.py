from django.shortcuts import render, redirect
from .models import Employee

# Mapa polskich znaków diakrytycznych i ich odpowiedników bez diakrytyków
POLISH_CHARACTERS_MAP = {
    'ą': 'a',
    'ć': 'c',
    'ę': 'e',
    'ł': 'l',
    'ń': 'n',
    'ó': 'o',
    'ś': 's',
    'ż': 'z',
    'ź': 'z',
}

def index(request):
    """Widok obsługujący stronę główną."""
    if request.method == 'POST':
        # Pobranie danych z formularza POST
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        # Generowanie adresu e-mail
        email = generate_email(first_name, last_name)
        # Tworzenie obiektu pracownika i zapisanie go w bazie danych
        employee = Employee.objects.create(first_name=first_name, last_name=last_name, email=email)
        employee.save()
        # Przekierowanie użytkownika na stronę wyników
        return redirect('result')
    # Renderowanie strony głównej
    return render(request, 'index.html')

def generate_email(first_name, last_name):
    """Funkcja generująca adres e-mail na podstawie imienia i nazwiska."""
    domain = 'nasza_firma.com' # Tutaj ustalamy nazwę domeny
    # Normalizacja polskich znaków diakrytycznych w imieniu i nazwisku
    first_name_normalized = normalize_polish_characters(first_name)
    last_name_normalized = normalize_polish_characters(last_name)
    # Generowanie adresu e-mail w formacie imie.nazwisko@nasza_firma.com
    email = f"{first_name_normalized.lower()}.{last_name_normalized.lower()}@{domain}"
    num = 1
    # Sprawdzanie, czy adres e-mail już istnieje w bazie danych
    while Employee.objects.filter(email=email).exists():
        email = f"{first_name_normalized.lower()}.{last_name_normalized.lower()}{num}@{domain}"
        num += 1
    return email

def normalize_polish_characters(text):
    """Funkcja zamieniająca polskie znaki diakrytyczne na ich odpowiedniki bez diakrytyków."""
    for polish_char, replacement in POLISH_CHARACTERS_MAP.items():
        text = text.replace(polish_char, replacement)
    return text

def result(request):
    """Widok obsługujący stronę wyników."""
    try:
        # Pobranie adresu e-mail ostatniego pracownika z bazy danych
        latest_employee = Employee.objects.latest('id')
        email = latest_employee.email
    except Employee.DoesNotExist:
        email = None
    # Renderowanie strony wyników
    return render(request, 'result.html', {'email': email})
