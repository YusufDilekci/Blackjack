import random


class Cards:
    def __init__(self):
        self.cards = {'H1': 11, 'H2': 2, 'H3': 3, 'H4': 4, 'H5': 5, 'H6': 6, 'H7': 7, 'H8': 8, 'H9': 9, 'H10': 10,
                      'HK': 10, 'HQ': 10, 'HJ': 10,
                      'D1': 11, 'D2': 2, 'D3': 3, 'D4': 4, 'D5': 5, 'D6': 6, 'D7': 7, 'D8': 8, 'D9': 9, 'D10': 10,
                      'DK': 10, 'DQ': 10, 'DJ': 10,
                      'C1': 11, 'C2': 2, 'C3': 3, 'C4': 4, 'C5': 5, 'C6': 6, 'C7': 7, 'C8': 8, 'C9': 9, 'C10': 10,
                      'CK': 10, 'CQ': 10, 'CJ': 10,
                      'S1': 11, 'S2': 2, 'S3': 3, 'S4': 4, 'S5': 5, 'S6': 6, 'S7': 7, 'S8': 8, 'S9': 9, 'S10': 10,
                      'SK': 10, 'SQ': 10, 'SJ': 10,
                      }
        self.my_cards = []
        self.computer_cards = []
        self.chosen_cards = {}
        self.total_my_cards = 0
        self.total_computer_cards = 0


    def shuffle_distribute_cards(self):
        ''' Shuffle the cards and spot them.'''
        for _ in range(2):
            key_cards = random.choice(list(self.cards))
            self.my_cards.append(key_cards)
            self.chosen_cards[key_cards] = self.cards[key_cards]

        card_to_computer = random.choice(list(self.cards))
        self.computer_cards = [card_to_computer]
        self.chosen_cards[card_to_computer] = self.cards[card_to_computer]
       

    def draw_card(self, player):
        '''Oyuncu kart çekmek istediğinde bu fonksiyon kullanılır'''
        index_number = random.randint(0, len(self.cards)-1)
        cards_list = list(self.cards)
        card_name = cards_list[index_number]
        player.append(card_name)
        self.chosen_cards[card_name] = self.cards[card_name]


    def show_card(self):
        '''Kartlar açılır'''
        print(f"That's my cards: {self.my_cards}\nHere computer cards: {self.computer_cards}")

    # def calculate_cards_value(self, type_player, total_card):
    #     '''Her iki tarafında elinde bulunan kartların değerleri hesaplanır Global varaible total card sorunu'''
    #
    #     for key in type_player:
    #         total_card += self.chosen_cards[key]
    #         if (total_card > 21) and (('H1' in type_player) or ('D1' in type_player) or
    #                                            ('C1' in type_player) or ('S1' in type_player)):
    #             total_card -= 10
    #
    #     return total_card

    def calculate_player(self):
        for key in self.my_cards:
            self.total_my_cards += self.chosen_cards[key]
            if (self.total_my_cards > 21) and (('H1' in self.my_cards) or ('D1' in self.my_cards) or
                                          ('C1' in self.my_cards) or ('S1' in self.my_cards)):
                self.total_my_cards -= 10

        player_result = self.total_my_cards
        self.total_my_cards = 0
        return player_result



    def calculate_computer(self):

        for key in self.computer_cards:
            self.total_computer_cards += self.chosen_cards[key]
            if (self.total_computer_cards > 21) and (('H1' in self.computer_cards) or ('D1' in self.computer_cards) or
                                                     ('C1' in self.computer_cards) or ('S1' in self.computer_cards)):
                self.total_computer_cards -= 10

        computer_result = self.total_computer_cards
        self.total_computer_cards = 0
        return computer_result