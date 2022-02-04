from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Deck(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="decks")
    title = models.CharField(max_length=30)
    creation_date = models.DateTimeField(auto_now_add=True)


class Card(models.Model):
    DECK_TYPES = (
        ("P", "Perfect"),
        ("S", "Self"),
        ("C", "Checkbox"),
    )

    deck = models.ForeignKey(Deck, on_delete=models.CASCADE, related_name="cards")
    front = models.CharField(max_length=300)
    back = models.CharField(max_length=300)
    deck_type = models.CharField(max_length=1, choices=DECK_TYPES, default="S")
