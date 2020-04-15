print('Welcome to Tic Tac Toe!')

while True:
    the_board=[' ']*10
    player1_marker,player2_marker=player_input()
    turn = choose_first()
    print(turn + ' will go first.')    
    play_game=input('Ready to play? Y or N')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on= False
    
    while game_on:
        if turn == 'player1':
            display_board(the_board)
            position=player_choice(the_board)
            place_marker(the_board, player1_marker,position)
            
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print("player1 has won")     
                game_on=False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("Tie game")
                    break
                else:
                    turn= 'Player2'
        else:
            display_board(the_board)
            position=player_choice(the_board)
            place_marker(the_board, player2_marker,position)
            
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print("player2 has won")     
                game_on=False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("Tie game")
                    break
                else:
                    turn = 'player1'
                    
    if not replay():
        break
        