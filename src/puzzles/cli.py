import click
from .nqueens import solve_nqueens
from .visualize import visualize_nqueens
from .chess_utils import solution_to_chess_notation

@click.command()
@click.argument('n', type=int)
@click.option('--save', '-s', help='Save visualization to file path')
def nqueens(n: int, save: str) -> None:
    """Solve and visualize the N-Queens puzzle for a given board size."""
    solution = solve_nqueens(n)
    if solution is None:
        click.echo(f"No solution exists for {n}-Queens puzzle")
        return
    
    chess_positions = solution_to_chess_notation(solution)
    click.echo(f"Found solution for {n}-Queens puzzle: {chess_positions}")
    visualize_nqueens(solution, save)

if __name__ == '__main__':
    nqueens()
