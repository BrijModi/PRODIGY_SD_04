
import tkinter as tk
from tkinter import messagebox


def find_empty(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return (row, col)
    return None

# To checks that the number is vaild according to the sudoku rule or not 
def is_valid(board, row, col, num):
    # Checking rows and columns
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    
    # Checking the 3x3 box
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    
    return True


def solve_sudoku(board):
    empty_cell = find_empty(board)
    if not empty_cell:
        return True
    row, col = empty_cell

    # Trying numbers from 1 to 9
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0
    
    return False

def get_board_from_entries():
    board = []
    for row in range(9):
        current_row = []
        for col in range(9):
            val = entries[row][col].get()
            current_row.append(int(val) if val else 0)
        board.append(current_row)
    return board

def set_board_to_entries(board):
    for row in range(9):
        for col in range(9):
            entries[row][col].delete(0, tk.END)
            entries[row][col].insert(0, str(board[row][col]))

def solve_button_handler():
    board = get_board_from_entries()
    if solve_sudoku(board):
        set_board_to_entries(board)
        messagebox.showinfo("Sudoku Solver", "Sudoku Solved!")
    else:
        messagebox.showinfo("Sudoku Solver", "No solution exists")

# Create the main window
root = tk.Tk()
root.title("Sudoku Solver")

# Create a grid of Entry widgets
entries = [[None for _ in range(9)] for _ in range(9)]
for row in range(9):
    for col in range(9):
        entries[row][col] = tk.Entry(root, width=2, font=("Comic Sans", 18), justify="center")
        entries[row][col].grid(row=row, column=col, padx=8, pady=6)

# Create and place the Solve button
solve_button = tk.Button(root, text="Solve", font=("Comic Sans", 12), relief="raised", border=3, command=solve_button_handler)
solve_button.grid(row=9, column=0, columnspan=9, pady=10)

# Run the Tkinter event loop
root.mainloop()
