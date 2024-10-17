'''
 X | O | X
---+---+---
 O | O | X    
---+---+---
   | X | 
'''

import random
from copy import deepcopy


def print_board_and_legend(board):
    for i in range(3):
        line1 = " " +  board[i][0] + " | " + board[i][1] + " | " +  board[i][2]
        line2 = "  " + str(3*i+1)  + " | " + str(3*i+2)  + " | " +  str(3*i+3) 
        print(line1 + " "*5 + line2)
        if i < 2:
            print("---+---+---" + " "*5 + "---+---+---")
        
    
    
def make_empty_board():
    board = []
    for i in range(3):
        board.append([" "]*3)
    return board

def move(square_num):
    coord = [(square_num-1)//3, (square_num-1)%3]
    return coord

def put_in_board(board, mark, square_num):
    board[move(square_num)[0]][move(square_num)[1]] = mark

def winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != " ":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]
    return False

def get_free_squares(board):
    free = []
    for i in board:
        for j in range(len(i)):
            if i[j] == " ":
                free.append([board.index(i), j])
    return free

def best_move(board, mark):
    for i in get_free_squares(board):
        board_test = deepcopy(board)
        board_test[i[0]][i[1]] = mark
        if winner(board_test) == mark:
            return i
    for i in get_free_squares(board):
        board_test = board
        mark_test = "X" if mark == "O" else "O"
        for j in get_free_squares(board):
            board_test = deepcopy(board)
            board_test[j[0]][j[1]] = mark_test
            if winner(board_test) == mark_test:
                return j
    return random.choice(get_free_squares(board))

def make_random_move(board, mark):
    move = best_move(board, mark)
    board[move[0]][move[1]] = mark
    return board
    
if __name__ == '__main__':
    board = make_empty_board()
    print_board_and_legend(board)    
    
    while winner(board) == False:
        square_num = int(input("player 1: "))
        put_in_board(board, "X", square_num)
        print_board_and_legend(board)
        print("\n\n")
        if winner(board):
            break
        board = make_random_move(board, "O")
        print_board_and_legend(board)
        print("\n\n")

    print(f'{winner(board)} wins!')