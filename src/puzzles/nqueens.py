from typing import List, Optional
import numpy as np

def solve_nqueens(n: int) -> Optional[List[int]]:
    """
    Solve the N-Queens puzzle for a given board size.
    Returns a list where index is row and value is column position of queen,
    or None if no solution exists.
    """
    def is_safe(board: List[int], row: int, col: int) -> bool:
        for i in range(row):
            if (board[i] == col or 
                board[i] - i == col - row or 
                board[i] + i == col + row):
                return False
        return True
    
    def solve(board: List[int], row: int) -> bool:
        if row >= n:
            return True
            
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                if solve(board, row + 1):
                    return True
                board[row] = -1
                
        return False

    board = [-1] * n
    if solve(board, 0):
        return board
    return None
