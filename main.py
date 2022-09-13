from cards import Cards
card = Cards()



balance = 1500
add_card= 0
is_game_on = True
is_money_enough = True
is_add_card = True


while is_game_on and is_money_enough:
    money = int(input('Write the bet amount: '))

    if money > balance:
        print("Get the fuck out! You don't have enough money.")
        is_money_enough = False
    else:
        balance -= money
        card.shuffle_distribute_cards()
        card.show_card()

       
        if( card.calculate_player() == 21):
            print("You won")
            is_game_on = False
        else:
      
            while is_add_card:
                add_card = input('Do you wanna get a card: ').lower()
                if add_card == 'yes':
                    card.draw_card(card.my_cards)
                    card.show_card()

                    if card.calculate_player() == 21:
                        card.draw_card(card.computer_cards)
                        card.show_card()
                        print('You won')
                        is_add_card = False

                    if  card.calculate_player() > 21:
                        card.draw_card(card.computer_cards)
                        card.show_card()
                        print('Computer won')
                        is_add_card = False

                elif add_card == 'no':
                    is_add_card = False

                else:
                    print('Please enter (yes/no): ')


            if add_card == 'no':  
               
                while  card.calculate_computer() < 17:
                    card.draw_card(card.computer_cards)
                      
                card.show_card()
                
                computer = card.calculate_computer()
                player = card.calculate_player()

                if player == 21 or computer == 21:
                    if player == 21 and computer != 21:
                        print('You won')
                    elif computer == 21 and player != 21:
                        print('Computer won')
                    else:
                        print('Draw')

                elif player < computer < 21:
                    print('Computer Won')
                
                elif computer < player < 21 or computer > 21:
                    print('You won')

            
                else:
                    print('hiçbir koşula girmedim')

            is_game_on = False



# random kart seçme ve kartın değerini alma
# import random
# a = {'ali': 3, 'beyza': 5, 'saffet': 8, 'ayşe': 10}

# b = {key: item for key,item in a.items()}
# print(b)


# index = random.randint(0,3)
# print(index)
# b = list(a)

# print(b[index])


# b = [1,23,44,5]


# if '1' in b:
#     print('A')

