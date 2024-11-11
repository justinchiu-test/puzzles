from typing import List

def index_to_chess(row: int, col: int) -> str:
    """Convert zero-based indices to chess notation (e.g., 0,0 -> 'a1')"""
    return f"{chr(ord('a') + col)}{row + 1}"

def solution_to_chess_notation(solution: List[int]) -> List[str]:
    """Convert a solution list to chess notation positions"""
    return [index_to_chess(row, col) for row, col in enumerate(solution)]

def chess_to_index(position: str) -> tuple[int, int]:
    """Convert chess notation to zero-based indices (e.g., 'a1' -> (0,0))"""
    col = ord(position[0].lower()) - ord('a')
    row = int(position[1]) - 1
    return (row, col)
