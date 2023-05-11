import numpy as np
import random
from tabulate import tabulate


# filling 3 rows of the board with numbers => get 3 unique squares
# variable 'square' - set of columns' numbers for each square
def line_of_3_squares(board, numb, square, square_rows):
    '''filling one line of 3x3 squares with numbers'''

    squares1 = sum(square,[])
    squares2 = sum([square[1], square[2], square[0]],[])
    squares3 = sum([square[2], square[0], square[1]],[])
    for i in squares1:  
        board[square_rows[0],i]= numb[squares1[i]]
       
    for i in squares2:
        board[square_rows[1],i]= numb[squares2[i]]
       
    for i in squares3:
        board[square_rows[2],i]= numb[squares3[i]]  
        



def fill_board(board, numb, square):
    '''filling the array with numbers'''
    line_of_3_squares(board, numb, square, square[0])
   
    nb = numb.pop(0)
    numb.insert(8, nb)
    line_of_3_squares(board, numb, square, square[1])
    
    nb = numb.pop(0)
    numb.insert(8, nb)
    line_of_3_squares(board, numb, square, square[2])
    


# swapping columns in 3x3 squares
def swap_column_in__squares(board, square):
    random.shuffle(square[0])
    board[:, [0,1,2]] = board[:, square[0]]

    random.shuffle(square[1])
    board[:, [3,4,5]] = board[:, square[1]]

    random.shuffle(square[2])
    board[:, [6,7,8]] = board[:, square[2]]



# checking compliance with sudoku rules 
def find_non_unique(board):
    '''finding rows with duplicates'''
    rows = []
    for i in range(len(numbers)):
        row = np.unique(board[i])
        if len(row)< len(numbers):
            rows.append(i)
    return rows



# -----START--------
print"\n  SUDOKU \n"
input("")
while True:
    game_board = np.zeros([9,9], dtype = "int")

    numbers =[1,2,3,4,5,6,7,8,9]

    # small squares' column indices
    sq_index = [[0,1,2], [3,4,5], [6,7,8]]

    # mixing numbers
    random.shuffle(numbers)

    # creating game_board
    fill_board(game_board, numbers, sq_index )

    # swapping columns in 3x3 squares
    swap_column_in__squares(game_board, sq_index)

    print(tabulate(game_board, tablefmt='grid'))

    # checking compliance with sudoku rules
    row_num = find_non_unique(game_board)
    col_num = find_non_unique(game_board.transpose())

    if len(row_num) >0:
        print(f"\nNumery wierszy zawierających duplikaty: \n{row_num}")
    else:
        print("\nNie ma wierszy zawierających duplikaty.")

    if len(col_num) >0:
        print(f"Numery kolumn zawierających duplikaty: \n{col_num}")
    else:
        print("Nie ma kolumn zawierających duplikaty.")

    repeat = input("\nNowa tablica?  (t/n)")
    if repeat in ["N", "n"]:
        break
