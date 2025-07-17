from random import randrange
def display_board(board):
    for i in range(3):
        print('+-------'*3,'+',sep="")
        print('|       '*3,'|',sep="")
        for j in range(3):
            print('|   {0}   '.format(board[i][j]),end="")
        print('|')
        print('|       |       |       |')
    print('+-------'*3,'+',sep="")
        
def enter_move(board):
    while True:
        try:
          flag = True
          mov = int(input("Enter Your move: "))
          if mov<1 or mov>9:
              print('No such a move exists!! RETRY')
          else:
             ind =mov- 1
             row = ind//3
             col = (ind % 3)
             if board[row][col]== mov:
                 board[row][col]='o'
                 break
             else :
                 print("INVALID MOVE RETRY!!!")
        except :
            print("INVALID !! ENTER A VALID MOVE")
         
def make_list_of_free_fields(board):
    free_sq = []
  
    for i in range(3):
        for j in range(3):
            if board[i][j] not in ['o','x']:
                free_sq.append((i,j))
          
    return free_sq

def victory_for(board, sign):
    for i in range(3):
        if all(board[i][j]==sign for j in range(3)) or all(board[j][i]==sign for j in range(3)):
            return True       
        if all(board[j][j]==sign for j in range(3)) or all(board[j][2-j]==sign for j in range(3)):
            return True
    return False

def draw_move(board):
    
    free_sq = make_list_of_free_fields(board)
    size = len(free_sq)
    if size>0:
       index = randrange(size)
       row , col = free_sq[index]
       board[row][col]='x'

board = [[1,2,3],[4,5,6],[7,8,9]]
display_board(board)
print('Start with your move!!')
while True :
        enter_move(board)
        display_board(board)
        player = victory_for(board, 'o')
       
        if player:
            print("CONGRATULATIONS!! You won.\nGame Is Over!!")
            break
        print()
        print("Robot's Move")
        draw_move(board)
        display_board(board)
        comp = victory_for(board, 'x')
        
        if comp:
            print("You Lose!!.\nGame Is Over!!")
            break
        free_fields= make_list_of_free_fields(board)
        isComplete = len(free_fields)
        if isComplete == 0:
            print("Match is Draw!!")
            break
        