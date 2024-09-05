import os
import django

# Configurar o ambiente Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from restaurant.models import Restaurant


def print_history_summary(restaurant):
    """
    Resumo das ações realizadas no histórico do restaurante.
    history_type pode ser:
        '+': Criação.
        '~': Atualização.
        '-': Exclusão.
    """
    history = restaurant.history.all()
    for record in history:
        print(f"Data: {record.history_date}, Ação: {record.history_type}, Usuário: {record.history_user}")


def print_field_changes(restaurant):
    """
    Alterações nos campos entre versões do registro no histórico do restaurante.
    """
    history = restaurant.history.all()
    for record in history:
        previous = record.prev_record
        if previous:
            # Comparando os valores dos campos
            for field in record.instance._meta.fields:
                old_value = getattr(previous, field.name, None)
                new_value = getattr(record, field.name, None)
                if old_value != new_value:
                    print(f"Campo {field.name} alterado de {old_value} para {new_value}")


def print_all_history(restaurant):
    """
    resumo do histórico e alterações nos campos.
    """
    print("Resumo do Histórico:")
    print_history_summary(restaurant)
    print("\nAlterações nos Campos:")
    print_field_changes(restaurant)


if __name__ == "__main__":
    restaurant = Restaurant.objects.first()
    if restaurant:
        print_all_history(restaurant)
    else:
        print("Nenhum restaurante encontrado.")
