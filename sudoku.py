'''
1. Pick an empty space
2. Try all possible numbers
3. Find one that works
4. Repeat
5. Backtrack

solve_sudoku: This function uses a backtracking algorithm to solve the Sudoku puzzle recursively.
It first checks if there are any empty locations on the board. If not, it means the puzzle is solved and returns True.
Otherwise, it finds an empty location and tries numbers from 1 to 9. For each number, it checks if it's a valid move
(i.e., it doesn't violate any Sudoku rules). If it's valid, it assigns the number to the current location and recursively
calls itself. If the recursive call returns True, it means a solution is found and it returns True. Otherwise,
it resets the current location to 0 and tries the next number. If no number works, it returns False.

find_empty_location: This function finds the next empty location (represented by 0) on the board.
It iterates over each cell and returns the row and column of the first empty location it finds.
If there are no empty locations, it returns None.

is_valid_move: This function checks if a number is a valid move for a given location. It checks if the number already
exists in the same row, column, or the 3x3 grid that contains the location. If it finds a duplicate, it returns False.
Otherwise, it returns True.
'''

board = [
    [5,6,8,3,0,9,4,0,2],
    [0,0,2,0,0,6,0,0,0],
    [0,0,7,4,0,2,6,3,0],
    [0,8,5,0,0,4,1,0,0],
    [2,0,9,0,3,0,7,0,6],
    [7,0,0,0,6,1,0,0,9],
    [9,0,0,5,0,3,0,1,7],
    [0,0,0,0,0,7,0,0,0],
    [0,0,3,1,9,0,2,6,0]
]

def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end = "")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end = "")

def find_empty(bo):
    for i, row in enumerate(bo):
        for j, val in enumerate(row):
            if val == 0:
                return (i,j)

def is_valid_move(bo, num, pos):

    #Checks Row
    for i in range(len(bo[0])):
         if bo[pos[0]][i] == num and pos[1] != i:
             return False

    #Checks Column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    #Checks box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True

def solve(bo):

    find = find_empty(bo)
    if not find:
        return True
    else:
        row,col = find

    for i in range(1,10):
        if is_valid_move(bo, i, (row,col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False

print_board(board)
solve(board)
print("\n" + "\n")
print_board(board)
