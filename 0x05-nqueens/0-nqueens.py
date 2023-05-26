#!/usr/bin/python3
"""Nqueens module."""
import sys


def is_safe(board, row, col):
    """Check if the current position is safe from attacks."""
    for i in range(row):
        if board[i] == col or \
           board[i] == col - (row - i) or \
           board[i] == col + (row - i):
            return False
    return True

def solve_nqueens(board, row, n, solutions):
    """ All queens are successfully placed, add the solution to the list."""
    if row == n:
        solutions.append([[r, c] for r, c in enumerate(board)])
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(board, row + 1, n, solutions)
            board[row] = -1

def print_solutions(solutions):
    """Print solution."""
    for sol in solutions:
        print(sol)
    print()

def nqueens(n):
    """Initialize the chessboard."""
    board = [-1] * n
    solutions = []
    solve_nqueens(board, 0, n, solutions)
    print_solutions(solutions)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    nqueens(N)
