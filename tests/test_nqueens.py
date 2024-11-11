import pytest
from puzzles.nqueens import solve_nqueens
from puzzles.chess_utils import solution_to_chess_notation

def test_solve_nqueens():
    # Test known solutions
    solution4 = solve_nqueens(4)
    assert solution4 == [1, 3, 0, 2]  # One valid solution for n=4
    assert solution_to_chess_notation(solution4) == ['b1', 'd2', 'a3', 'c4']
    
    solution1 = solve_nqueens(1)
    assert solution1 == [0]  # Trivial case
    assert solution_to_chess_notation(solution1) == ['a1']
    
    # Test impossible case
    assert solve_nqueens(2) is None
    assert solve_nqueens(3) is None
    
    # Test larger boards have valid solutions
    for n in [5, 6, 7, 8]:
        solution = solve_nqueens(n)
        assert solution is not None
        assert len(solution) == n
        # Verify all queens are on different rows and columns
        assert len(set(solution)) == n
        # Verify chess notation conversion
        chess_positions = solution_to_chess_notation(solution)
        assert len(chess_positions) == n
        assert all(len(pos) == 2 for pos in chess_positions)
        assert all(pos[0] in 'abcdefgh'[:n] for pos in chess_positions)
        assert all(pos[1] in '12345678'[:n] for pos in chess_positions)
