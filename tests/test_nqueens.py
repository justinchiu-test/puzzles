import pytest
from puzzles.nqueens import solve_nqueens

def test_solve_nqueens():
    # Test known solutions
    assert solve_nqueens(4) == [1, 3, 0, 2]  # One valid solution for n=4
    assert solve_nqueens(1) == [0]  # Trivial case
    
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
