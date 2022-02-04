from rest_framework import serializers
from django.contrib.auth.models import User
from decks.models import Deck, Card


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = (
            "front",
            "back",
            "deck_type",
        )


class DeckSerializer(serializers.ModelSerializer):
    cards = CardSerializer(many=True, read_only=True)

    class Meta:
        model = Deck
        fields = (
            "title",
            "creation_date",
            "cards",
        )


class UserSerializer(serializers.ModelSerializer):
    decks = DeckSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "decks",
        )
