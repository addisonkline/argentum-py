from collections import Counter
from itertools import combinations
from src.game.cards import Card

def sort_hand(hand: list[Card]) -> list[Card]:
    """
    Return the given 5-card hand, but sorted in descending order by numeric value.
    """
    hand_sorted: list[Card] = sorted(hand, key=lambda card: card.value_numeric, reverse=True)
    return hand_sorted

def has_straight_flush(hand: list[Card]) -> bool:
    """
    Return True if a given 5-card hand has a straight flush.
    """
    return (has_straight(hand) and has_flush(hand))

def has_four_kind(hand: list[Card]) -> bool:
    """
    Return True if a given 5-card hand has a four-of-a-kind.
    """
    value_counts = Counter(card.value_numeric for card in hand)
    return 4 in value_counts.values()

def has_full_house(hand: list[Card]) -> bool:
    """
    Returns True if a given 5-card hand has a full house.
    """
    value_counts = Counter(card.value_numeric for card in hand)
    return (
        len(value_counts) == 2 and
        3 in value_counts.values()
    )

def has_flush(hand: list[Card]) -> bool:
    """
    Returns True if a given 5-card hand has a flush.
    """
    return (
        hand[0].suit == hand[1].suit and
        hand[1].suit == hand[2].suit and 
        hand[2].suit == hand[3].suit and
        hand[3].suit == hand[4].suit
    )

def has_straight(hand: list[Card]) -> bool:
    """
    Returns True if a given 5-card hand has a straight.
    """
    return (
        hand[0].value_numeric == hand[1].value_numeric + 1 and
        hand[1].value_numeric == hand[2].value_numeric + 1 and
        hand[2].value_numeric == hand[3].value_numeric + 1 and
        hand[3].value_numeric == hand[4].value_numeric + 1
    )

def has_three_kind(hand: list[Card]) -> bool:
    """
    Returns True if a given 5-card hand has a three-of-a-kind.
    """
    value_counts = Counter(card.value_numeric for card in hand)
    return 3 in value_counts.values()

def has_two_pair(hand: list[Card]) -> bool:
    """
    Returns True if a given 5-card hand has a two pair.
    """
    value_counts = Counter(card.value_numeric for card in hand)
    pairs = sum(1 for count in value_counts.values() if count == 2)
    return pairs == 2

def has_pair(hand: list[Card]) -> bool:
    """
    Returns True if a given 5-card hand has a pair.
    """
    value_counts = Counter(card.value_numeric for card in hand)
    return 2 in value_counts.values()

def score_hand(hand: list[Card], table: list[Card]) -> float:
    """
    Determine a score for a given hand and given table cards. 
    The hand with the higher numerical score always wins.
    """
    all_cards: list[Card] = hand + table
    all_five_card_hands = list(combinations(all_cards, 5))
    scores: list[float] = []
    # iterate through each possible combination of 5 cards taken from the 2-card hand and the 5-card table
    for hand_possible in all_five_card_hands:
        score: float = 0.0
        hand_possible = sort_hand(hand_possible)

        # step 1: determine first part of numeric score based on the kind of hand
        if (has_straight_flush(hand_possible)):
            score += 8
        elif (has_four_kind(hand_possible)):
            score += 7
        elif (has_full_house(hand_possible)):
            score += 6
        elif (has_flush(hand_possible)):
            score += 5
        elif (has_straight(hand_possible)):
            score += 4
        elif (has_three_kind(hand_possible)):
            score += 3
        elif (has_two_pair(hand_possible)):
            score += 2
        elif (has_pair(hand_possible)):
            score += 1
        else: # high card only
            score += 0

        # step 2: determine next part of numeric score based on the 5 best cards
        score += (hand_possible[0].value_numeric / 100) + (hand_possible[1].value_numeric / (100**2)) + (hand_possible[2].value_numeric / (100**3)) + (hand_possible[3].value_numeric / (100**4)) + (hand_possible[4].value_numeric / (100**5))

        scores.append(score)
    
    return max(scores)
    
