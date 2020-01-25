import random


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return ' of '.join((self.value, self.suit))


class Deck:
    def __init__(self):
        self.cards = [Card(s, v) for s in ['spades', 'clubs', 'hearts', 'diamonds'] for v in
                      ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']]

    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) > 1:
            return self.cards.pop(0)


class Hand:
    def __init__(self, dealer=False):
        self.dealer = dealer
        self.cards = []
        self.values = 0

    def add_cards(self, card):
        self.cards.append(card)

    def calculate_value(self):
        self.value = 0
        has_ace = False
        for card in self.cards:
            if card.value.isnumeric():
                self.value += int(card.value)
            else:
                if card.value == 'A':
                    has_ace = True
                    self.value += 11
                else:
                    self.value += 10
        if has_ace and self.value > 21:
            self.value -= 10

    def get_value(self):
        self.calculate_value()
        return self.value

    def display(self):
        if self.dealer:
            print('hidden')
            print(self.cards[1])
        else:
            for card in self.cards:
                print(card)
            print('value : ', self.get_value())


class Game:
    def __init__(self):
        playing = True
        while playing:
            self.deck = Deck()
            self.deck.shuffle()

            self.player_hand = Hand()
            self.dealer_hand = Hand(dealer=True)

            for i in range(2):
                self.player_hand.add_cards(self.deck.deal())
                self.dealer_hand.add_cards(self.deck.deal())

            print('Your hand is: ')
            self.player_hand.display()
            print()
            print('Dealer\'s Hands is:')
            self.dealer_hand.display()

            game_over = False
            while not game_over:
                player_has_blackjack, dealer_has_blackjack = self.check_for_blackjack()

                if player_has_blackjack or dealer_has_blackjack:
                    game_over = True
                    self.show_blackjack_results(player_has_blackjack, dealer_has_blackjack)
                    continue

                choice = input('Please choose [Hit/Stick]').lower()
                while choice not in ['hit', 'h', 'stick', 's']:
                    choice = input('Please enter the right input [hit/stick]').lower()
                if choice in ['hit', 'h']:
                    self.player_hand.add_cards(self.deck.deal())
                    self.player_hand.display()
                    if self.player_is_over():
                        print('You have lost!')
                        game_over = True
                else:
                    print("Final results ")
                    print('your hand: ', self.player_hand.get_value())
                    print('Dealer\'s hand: ', self.dealer_hand.get_value())

                    if self.player_hand.get_value() > self.dealer_hand.get_value():
                        print('You Win!')
                    elif self.player_hand.get_value() == self.dealer_hand.get_value():
                        print('Tie!')
                    else:
                        print('Dealer wins!')
                    game_over = True
            again = input('Play again? [Y/N] ').lower()
            while again not in ['y', 'n', 'yes', 'no']:
                again = input('Please enter the right input [Y/N]').lower()
            if again == 'n':
                print('Thanks for playing!')
                playing = False
            else:
                game_over = False

    def check_for_blackjack(self):
        player = False
        dealer = False
        if self.player_hand.get_value() == 21:
            player = True
        if self.dealer_hand.get_value() == 21:
            dealer = True
        return player, dealer

    def show_blackjack_results(self, player_has_blackjack, dealer_has_blackjack):
        if player_has_blackjack and dealer_has_blackjack:
            print('Both players have blackjack! Draw!')
        elif player_has_blackjack:
            print('You have blackjack U win')
        elif dealer_has_blackjack:
            print('Dealer has blackjack! Dealer wins!')

    def player_is_over(self):
        return self.player_hand.get_value() > 21


if __name__ == '__main__':
    game = Game()
