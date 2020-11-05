
def display_board():
    
    print(board[7]+"  | "+board[8]+" | "+board[9])
    print('--------')
    print(board[4]+"  | "+board[5]+" | "+board[6])
    print('--------')
    print(board[1]+"  | "+board[2]+" | "+board[3])
    
    

def input_player():
    marker=''
    player2=''
    player1=''
    while (marker!='x') and (marker!='o'):
        marker=input("PLAYER 1:DO YOU WANT TO BE 'X' or 'O'")
    
    if marker=="x":
        player1="x"
        player2='o'
    else:
        palyer2="o"
    return (player1,player2)    

#player1_marker,player2_marker=input_player()



def board_marker(board,marker,position):
    board[position]=marker
    display_board()
    

def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

def space_check(board,postion):
    return board[postion]==''

def board_full(board):
    for i in range(1,10):
        if space_check(board,i):
            return False 
    
    return True

def player_choice(board):
    position=0
    while position not in[1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position=int(input("Enter your position (1-9)"))

    return position
        
    


def replay():
        print("Do you want to play again?")
        answer=input()

#-------------------------------        
print("WELCOME TO TIC_TAC_TOE :-)")
print("---------------------------\n")

board=['']*10
player1_marker,player2_marker=input_player()
turn=player1_marker


while(True):
    s=input("Are you ready to play? (Y/N)")
    if(s=='Y'or s=='y'):
        gameon=True
        display_board()
        while gameon:
            if(turn=='x'):
                position=player_choice(board)
                board_marker(board,"x",position)
                if win_check(board,"x"):
                    print("x has won")
                    gameon=False
                else:
                    if board_full(board):
                        print("GAME TIED")
                        gameon=False
                    else:
                        turn='o'
                
                    
                    
            else:
                position=player_choice(board)
                board_marker(board,"o",position)
                if win_check(board,"o"):
                    print("o has won")
                    gameon=False
                else:
                    if board_full(board):
                        print("GAME TIED")
                        gameon=False
                    else:
                        turn='x'
                        
            if gameon==False:
                board=['']*10
                    
    else:
        break
