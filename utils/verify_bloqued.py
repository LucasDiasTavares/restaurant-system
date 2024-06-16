from django.utils import timezone
from restaurant.models import VisitHistory, Rating, User, Restaurant


def can_rate(user, restaurant):
    last_visit = VisitHistory.objects.filter(user=user, restaurant=restaurant).order_by('-visit_date').first()
    if last_visit and last_visit.next_rating_date > timezone.now():
        return False
    return True


user = User.objects.create(username='example_user', email='user@example.com', first_name='Example', last_name='User')
restaurant = Restaurant.objects.create(
    name='Example Restaurant',
    address='123 Example St',
    city='Example City',
    state='EX',
    postal_code='12345',
    phone='123-456-7890',
    email='contact@examplerestaurant.com',
    cuisine_type='Italian',
    opening_hours='10:00 - 22:00',
    description='A great example restaurant.'
)

if can_rate(user, restaurant):
    rating = Rating(user=user, restaurant=restaurant, value=8)
    rating.save()
    visit_history = VisitHistory(user=user, restaurant=restaurant, rating=rating)
    visit_history.save()
else:
    print("You can only rate the same restaurant after 7 days.")
