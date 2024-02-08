#!/usr/bin/python3
"""
N Queens puzzle solver
"""

import sys


def is_safe(board, row, col, N):
    """
    Check if it's safe to place a queen at board[row][col]

    Args:
        board (list): The chessboard.
        row (int): The row to check.
        col (int): The column to check.
        N (int): The size of the chessboard.

    Returns:
        bool: True if safe, False otherwise.
    """
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def print_solutions(board):
    """
    Print the chessboard with queens placed.

    Args:
        board (list): The chessboard.
    """
    for row in board:
        print(row)


def solve_nqueens_util(board, col, N):
    """
    Utility function to solve N Queens problem using backtracking.

    Args:
        board (list): The chessboard.
        col (int): The current column to place a queen.
        N (int): The size of the chessboard.

    Returns:
        bool: True if a solution is found, False otherwise.
    """
    if col == N:
        print_solutions(board)
        return True

    res = False
    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            res = solve_nqueens_util(board, col + 1, N) or res
            board[i][col] = 0  # Backtrack if placing a queen in the
            # current position doesn't lead to a solution

    return res


def solve_nqueens(N):
    """
    Solve N Queens problem and print all solutions.

    Args:
        N (int): The size of the chessboard.
    """
    if not isinstance(N, int):
        print(f"Error: N must be an integer, got {N}")
        sys.exit(1)

    if N < 4:
        print(f"Error: N must be at least 4, got {N}")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]

    if not solve_nqueens_util(board, 0, N):
        print("No solution found")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        solve_nqueens(N)
    except ValueError:
        print(f"Error: N must be a number, got {sys.argv[1]}")
        sys.exit(1)
