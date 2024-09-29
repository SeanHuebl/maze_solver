from maze import Maze
from window import Window

def main() -> None:
    """
    Main function to initialize the window and maze, generate a random maze,
    solve it using DFS, and wait for the user to close the window.

    The function sets up the graphical window and maze using a 50x50 cell grid. 
    Walls are broken down recursively to generate the maze, which is solved 
    using Depth-First Search (DFS). Finally, it waits for the user to close 
    the window.

    Returns:
        None
    """
    
    win = Window(800, 600)  # Creates the window for visualizing the maze.
    
    cell_size_x = 25
    cell_size_y = 25  # Defines the grid resolution for the maze.
    
    # Initializes the maze with a dynamic size that fits within the window.
    maze = Maze(0, 0, win.width // cell_size_x, win.height // cell_size_y, cell_size_x, cell_size_y, win)
    
    # Ensure the maze has both an entrance and exit to guarantee solvability.
    maze._break_entrance_and_exit()
    
    # Randomly break walls to generate a solvable maze using DFS.
    maze._break_walls_r(0, 0)

    # Clear previous visit data to prepare for solving the maze.
    maze._reset_cells_visited()
    
    # Solve the maze using Depth-First Search (DFS).
    maze.solve()
    
    # Wait for the user to close the window before ending the program.
    win.wait_for_close()

if __name__ == "__main__":
    main()
