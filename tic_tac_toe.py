
#DICTIONAY FOR BOARD
board= {'one': ' ', 'two': ' ', 'three': ' ', 
        'four': ' ', 'five': ' ', 'six' : ' ',
        'seven': ' ', 'eight': ' ', 'nine': ' '}
print("one   ║ two   ║ three")
print("══════════════════════")
print("four  ║ five  ║ six")
print("══════════════════════")
print("seven ║ eight ║ nine")
print("\n")
moves=0
player=1
def box() :
    print(board['one']+'    ║'+board['two']+'    ║'+board['three'])
    print("══════════════════════")
    print(board['four']+'    ║'+board['five']+'    ║'+board['six'])
    print("══════════════════════")
    print(board['seven']+'    ║'+board['eight']+'    ║'+board['nine'])
    print("\n")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

"""def result() :
    if (board['one'] == 'X' and board['two'] == 'X'and board['three'] == 'X') :) or (board['seven'] == 'X' and board['eight'] == 'X' and board['nine']== 'X') or (board['two'] == 'X' and board['five'] == 'X' and  board['eight'] == 'X') or (board['three'] == 'X' and board['six'] == 'X' and board['nine'] == 'X') or (board['three'] == 'X' and board['five'] == 'X' and board['seven'] == 'X') :
        print("````PLAYER ONE WON`````` ")
    if board['one'] == 'X' and board['four'] == 'X' and board['seven'] == 'X' :
        print("````PLAYER ONE WON`````` ")
    if board['one'] == 'X' and board['five'] == 'X' and board['nine'] == 'X' :
        print("````PLAYER ONE WON`````` ")
    if board['four'] == 'X' and board['five'] == 'X' and  board['six'] == 'X' :
        print("````PLAYER ONE WON`````` ")
    elif (board['one'] == 'O' and board['two'] == 'O' and  board['three'] == 'O') or (board['one'] == 'O' and board['four'] == 'O' and board['seven'] == 'O') or (board['one'] == 'O' and board['five'] == 'O' and board['nine'] == 'O') or  (board['four'] == 'O' and board['five'] == 'O' and  board['six'] == 'O') or (board['seven'] == 'O' and board['eight'] == 'O' and board['nine']== 'O') or (board['two'] == 'O' and board['five'] == 'O' and  board['eight'] == 'O') or (board['three'] == 'O' and board['six'] == 'O' and board['nine'] == 'O') or (board['three'] == 'O' and board['five'] == 'O' and board['seven'] == 'O') :
        print("``````PLAYER TWO WON`````` ")
    else :
    
        print("``````MATCH DRAWN`````")    
        
"""
def result () :
    if board['one']=="X" and board['two']=="X" and board['three']=="X":
     print("\n~~~~~~~PLAYER 1 won~~~~~~~~")
    elif board['four']=="X" and board['five']=="X" and board['six']=="X":
     print("\n~~~~~~~~~~~PLAYER 1 won~~~~~~~~~~~")
    elif board['seven']=="X" and board['eight']=="X" and board['nine']=="X":
     print("\n~~~~~~~~~~~PLAYER 1 won~~~~~~~~~~~~")
    elif board['one']=="O" and board['two']=="O" and board['three']=="O":
     print("\n~~~~~~~~~~~PLAYER 2 won~~~~~~~~~~~~")
    elif board['four']=="O" and board['five']=="O" and board['six']=="O":
     print("\n~~~~~~~~~~~PLAYER 2 won~~~~~~~~~~~~")
    elif board['seven']=="O" and board['eight']=="O" and board['nine']=="O":
     print("\n~~~~~~~~~~~PLayer 2 won~~~~~~~~~~~")
    elif board['one'] == "X" and board['four'] == "X" and board['seven'] == "X":
     print("\n~~~~~~~~~~~PLAYER 1 won~~~~~~~~~~~~~")
    elif board['two'] == "X" and board['five'] == "X" and board['eight'] == "X":
     print("\n~~~~~~~~~~~~PLAYER 1 won~~~~~~~~~~~~~")
    elif board['three'] == "X" and board['six'] == "X" and board['nine'] == "X":
     print("\n~~~~~~~~~~~~~PLAYER 1 won~~~~~~~~~~~~")
    elif board['one'] == "O" and board['four'] == "O" and board['seven'] == "O":
     print("\n~~~~~~~~~~~~~~PLAYER 2 won~~~~~~~~~~~")
    elif board['two'] == "O" and board['five'] == "O" and board['eight'] == "O":
     print("\n~~~~~~~~~PLAYER 2 won~~~~~~~~~")
    elif board['three'] == "O" and board['six'] == "O" and board['nine'] == "O":
     print("\n~~~~~~~~~~~~PLAYER 2 won~~~~~~~~~~")
    elif board['one'] == "X" and board['five'] == "X" and board['nine'] == "X":
     print("\n~~~~~~~~~~~PLAYER 1 won~~~~~~~~")
    elif board['one'] == "O" and board['five'] == "O" and board['nine'] == "O":
     print("\n~~~~~~~~~PLAYER 2 won~~~~~~~~~")
    elif board['three'] == "O" and board['five'] == "O" and board['seven'] == "O":
     print("\n~~~~~~~~PLAYER 2 won~~~~~~~~")
    elif board['three'] == "O" and board['five'] == "O" and board['seven'] == "O":
     print("\n~~~~~~PLAYER 2 won~~~~~~~~~")
    else:
     if (moves==9) :
         print("!!!!....MATCH DRAWN....") 

#condition = result()
while True :
    box()
    if moves==9 : #or condition ==1 :
         break
    while True :
        if player == 1 :
            pl=input('Player one: ')
            if pl in board and board[pl] ==' ' :
                board[pl] = 'X'
                player=2
                break
            else :
                print("Wrong input...Enter again")
                continue
        else :
            p2=input("Player two: ")
            if p2 in board and board[p2] == ' ' :
                board[p2] = 'O'
                player=1
                break
            else :
                print("Wrong input...Enter again")
                continue
    moves+=1
    result()



        





