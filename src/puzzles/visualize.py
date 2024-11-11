import matplotlib.pyplot as plt
import numpy as np
from typing import List

def visualize_nqueens(solution: List[int], save_path: Optional[str] = None) -> None:
    """
    Visualize an N-Queens solution using matplotlib.
    Args:
        solution: List where index is row and value is column position of queen
        save_path: Optional path to save the visualization
    """
    n = len(solution)
    board = np.zeros((n, n))
    
    # Create checkered board pattern
    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == 0:
                board[i, j] = 0.8  # Light squares
            else:
                board[i, j] = 0.3  # Dark squares
    
    plt.figure(figsize=(8, 8))
    plt.imshow(board, cmap='gray')
    
    # Place queens
    for row, col in enumerate(solution):
        plt.plot(col, row, 'ro', markersize=20, label='Queen')
    
    plt.grid(True)
    plt.title(f'{n}-Queens Solution')
    plt.xticks(range(n))
    plt.yticks(range(n))
    
    if save_path:
        plt.savefig(save_path)
    else:
        plt.show()
    plt.close()
