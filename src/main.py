import random
from itertools import combinations
# internal imports
from src.game.cards import (
    Card,
    Deck
)
from src.game.player import (
    Player
)
from src.game.hand_ranker import (
    score_hand
)

class Game:
    def __init__(self):
        self.deck = Deck()
        self.player1 = Player("Player 1", 1000)
        self.player2 = Player("Player 2", 1000)
        self.community_cards = []
        self.pot = 0
        self.current_bet = 0
        
    def start_new_hand(self):
        # Reset everything for a new hand
        self.deck = Deck()
        self.deck.shuffle()
        self.community_cards = []
        self.pot = 0
        self.current_bet = 0
        self.player1.hand = []
        self.player2.hand = []
        self.player1.has_folded = False
        self.player2.has_folded = False
        
        # Switch dealer position
        self.player1.is_dealer = not self.player1.is_dealer
        
        # Deal cards
        self.deal_hole_cards()
        print(f'Player 1 hand: {self.player1.hand[0].identity}, {self.player1.hand[1].identity}')
        print(f'Player 2 hand: {self.player2.hand[0].identity}, {self.player2.hand[1].identity}')

        # Post blinds
        self.post_blinds()
        
        # Start betting rounds
        self.betting_round("pre-flop")
        if not self.hand_is_over():
            self.deal_flop()
            print(f'The table after the flop is: {self.community_cards[0].identity}, {self.community_cards[1].identity}, {self.community_cards[2].identity}')
            self.betting_round("flop")
        if not self.hand_is_over():
            self.deal_turn()
            print(f'The table after the turn is: {self.community_cards[0].identity}, {self.community_cards[1].identity}, {self.community_cards[2].identity}, {self.community_cards[3].identity}')
            self.betting_round("turn")
        if not self.hand_is_over():
            self.deal_river()
            print(f'The table after the river is: {self.community_cards[0].identity}, {self.community_cards[1].identity}, {self.community_cards[2].identity}, {self.community_cards[3].identity}, {self.community_cards[4].identity}')
            self.betting_round("river")
        
        if not self.hand_is_over():
            self.showdown()
    
    def deal_hole_cards(self):
        # Deal two cards to each player
        self.player1.hand = [self.deck.deal_card(), self.deck.deal_card()]
        self.player2.hand = [self.deck.deal_card(), self.deck.deal_card()]
    
    def deal_flop(self):
        # Deal three community cards
        self.community_cards.extend([self.deck.deal_card() for _ in range(3)])
    
    def deal_turn(self):
        # Deal one community card
        self.community_cards.append(self.deck.deal_card())
    
    def deal_river(self):
        # Deal one community card
        self.community_cards.append(self.deck.deal_card())
    
    def post_blinds(self):
        small_blind = 10
        big_blind = 20
        
        if self.player1.is_dealer:
            self.player1.chips -= small_blind
            self.player2.chips -= big_blind
        else:
            self.player2.chips -= small_blind
            self.player1.chips -= big_blind
        
        self.pot = small_blind + big_blind
        self.current_bet = big_blind
    
    def betting_round(self, round_name):
        # Implement betting logic here
        # This would include checking, betting, raising, calling, folding
        pass
    
    def hand_is_over(self):
        return self.player1.has_folded or self.player2.has_folded
    
    def showdown(self):
        # Evaluate hands and determine winner
        player1_best = self.get_best_hand(self.player1)
        player2_best = self.get_best_hand(self.player2)
        
        # Compare hands and award pot
        # (You'll need to implement hand comparison logic)
        if (player1_best > player2_best):
            print('Player 1 wins!')
            print(f'Score: {player1_best} vs. {player2_best}')
        elif (player2_best > player1_best):
            print('Player 2 wins!')
            print(f'Score: {player2_best} vs. {player1_best}')
        else: # tie
            print("It's a tie!")
            print(f'Score: {player1_best} vs. {player2_best}')
    
    def get_best_hand(self, player):
        # Get all seven cards (2 hole cards + 5 community cards)
        score = score_hand(hand=player.hand, table=self.community_cards)
        
        return score

# Example usage:
def play_game():
    game = Game()
    while True:
        game.start_new_hand()
        
        # Ask if players want to play another hand
        play_again = input("Play another hand? (y/n): ")
        if play_again.lower() != 'y':
            break

if __name__ == "__main__":
    play_game()