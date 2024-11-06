from pydantic import BaseModel
import random

class Card:
    value: str
    value_numeric: int
    suit: str
    identity: str

    def __init__(self, value: str, suit: str):
        self.value = value
        self.suit = suit
        self.value_numeric = self._generate_value_numeric(value)
        self.identity = self._generate_id(value, suit)

    def __eq__(self, value) -> bool:
        return self.identity == value.identity

    def _generate_value_numeric(self, value: str) -> int:
        match value:
            case 'A':
                return 14
            case 'K':
                return 13
            case 'Q':
                return 12
            case 'J':
                return 11
            case 'T':
                return 10
            case _:
                return int(value)
    
    def _generate_id(self, value: str, suit: str) -> str:
        return f"{value}{suit}"

class Deck:
    cards: list[Card]

    def __init__(self):
        self.cards = []
        suits = ['s', 'h', 'c', 'd']
        values = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
        
        for suit in suits:
            for value in values:
                self.cards.append(Card(value, suit))
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal_card(self):
        return self.cards.pop()    