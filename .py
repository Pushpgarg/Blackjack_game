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
