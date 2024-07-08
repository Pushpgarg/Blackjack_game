# importing necessary libraries
from art import logo
import random
import os 
clear = lambda: os.system('clear' if os.name == 'posix' else 'cls')
clear()

# initialising every list
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
player_cards=[]
computer_cards=[]
want_to_play = False

# for creating non stop game 
def asking_if_player_want_another_card():
    return input("Type 'y' to get another card, type 'n' to pass: ").lower()

def player_draw_a_card():
    player_new_card = random.randint(0,12)
    if((sum(player_cards)>10) and (player_new_card==0)):
        player_cards.append(1)
        return
    player_cards.append(cards[player_new_card])

def computer_draw_a_card():
    computer_new_card = random.randint(0,12)
    if((sum(player_cards)>10) and computer_new_card==0):
        computer_cards.append(1)
        return
    computer_cards.append(cards[computer_new_card])

def print_score():
    print(f"\tYour card: {player_cards},current score: {sum(player_cards)}")
    print(f"\tComputer's first card: {computer_cards[0]}")

def print_final_score():
    print(f"\tYour card: {player_cards}, current score: {sum(player_cards)}")
    print(f"\tComputer's card: {computer_cards}, current score: {sum(computer_cards)}")
    
# loop is used instead of Recursion to avoid stack overflow 
def new_game():
    while(True):
        game_over=False
        player_cards.clear()
        computer_cards.clear()

        asking_to_play = input("type 'y' to play blackjack or type 'n' to quit: ").lower()
        if(asking_to_play!='y'):
            break

        clear()

        while(True):
            print(logo)
            player_total_cards = len(player_cards)
            if (player_total_cards==0):
                player_draw_a_card()
                player_draw_a_card()
                computer_draw_a_card()
                computer_draw_a_card()
                
            print_score()

            
            player_want_another_card = asking_if_player_want_another_card()
            while(player_want_another_card == 'y'):
                player_draw_a_card()
                if(sum(player_cards)>21):
                    print_final_score()
                    print("Yon went over.You Lose 😥\n")
                    game_over = True
                    break
                elif(sum(player_cards)==21):
                    print_final_score()
                    print("You Win 😃\n")
                    game_over = True
                    break
                print_score()
                player_want_another_card = asking_if_player_want_another_card()

            if not game_over:
                if(player_want_another_card=='n'):
                    while(sum(computer_cards)<17):
                        computer_draw_a_card()
                        if(sum(computer_cards)>21):
                            print_final_score()
                            print("Computer went over. You Win! 😃\n")
                            game_over = True
                            break
            if not game_over:
                print_final_score()
                if(sum(player_cards) == sum(computer_cards)):
                    print("Draw! 🙄\n")
                elif(sum(player_cards) > sum(computer_cards)):
                    print("You Win! 😃 \n")
                elif(sum(player_cards) < sum(computer_cards)):
                    print("You lose! 🥲 \n")
            break

new_game()



    






