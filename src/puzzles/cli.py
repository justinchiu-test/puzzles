import click
from .nqueens import solve_nqueens
from .visualize import visualize_nqueens

@click.command()
@click.argument('n', type=int)
@click.option('--save', '-s', help='Save visualization to file path')
def nqueens(n: int, save: str) -> None:
    """Solve and visualize the N-Queens puzzle for a given board size."""
    solution = solve_nqueens(n)
    if solution is None:
        click.echo(f"No solution exists for {n}-Queens puzzle")
        return
    
    click.echo(f"Found solution for {n}-Queens puzzle: {solution}")
    visualize_nqueens(solution, save)

if __name__ == '__main__':
    nqueens()
