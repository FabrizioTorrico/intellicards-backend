from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Deck(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="decks")
    title = models.CharField(max_length=30)
    creationDate = models.DateTimeField(auto_now_add=True)


class Card(models.Model):
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE, related_name="cards")
    front = models.CharField(max_length=300)
    back = models.CharField(max_length=300)
