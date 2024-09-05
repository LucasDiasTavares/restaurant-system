import os
import django
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from restaurant.models import Restaurant, Menu, MenuItem, OpeningHours, CuisineType, UserPJ


def create_random_restaurant():
    fake = Faker()

    # Criar dono do restaurante
    owner = UserPJ.objects.create(
        username=fake.user_name(),
        email=fake.email()
    )

    # Cria o tipo de culinária
    cuisine = CuisineType.objects.create(name=fake.word())

    # Cria as horas de funcionamento
    opening_hours = []
    for day in ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sabado", "Domingo"]:
        open_time = fake.time_object()
        close_time = fake.time_object()
        if open_time > close_time:
            open_time, close_time = close_time, open_time
        opening_hours.append(
            OpeningHours.objects.create(
                day_of_week=day,
                open_time=open_time,
                close_time=close_time
            )
        )

    # Criar itens de menu
    menu_items = []
    for _ in range(5):
        item = MenuItem.objects.create(
            name=fake.word().capitalize(),
            description=fake.text(max_nb_chars=200),
            price=fake.random_number(digits=3),
            available=fake.boolean()
        )
        menu_items.append(item)

    # Cria o menu
    menu = Menu.objects.create(name=fake.word().capitalize())
    menu.item.add(*menu_items)

    # Criar o restaurante
    restaurant = Restaurant.objects.create(
        name=fake.company(),
        address=fake.address(),
        city=fake.city(),
        state=fake.state(),
        postal_code=fake.zipcode(),
        phone=fake.phone_number(),
        email=fake.company_email(),
        description=fake.text(max_nb_chars=500),
        owner=owner,
        cuisine_type=cuisine
    )

    # Associar horas de funcionamento e menu ao restaurante
    restaurant.opening_hours.add(*opening_hours)
    restaurant.menu.add(menu)

    print(f"Restaurante '{restaurant.name}' criado com sucesso!")


if __name__ == "__main__":
    create_random_restaurant()
