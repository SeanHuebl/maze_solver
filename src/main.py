from maze import Maze
from window import Window

def main() -> None:
    win = Window(800, 600)
    cell_size_x = 50
    cell_size_y = 50
    maze = Maze(0, 0, win.width // cell_size_x, win.height // cell_size_y, cell_size_x, cell_size_y, win)
    maze._break_entrance_and_exit()
    maze._break_walls_r(0, 0)
    maze._reset_cells_visited()
    maze.solve()
    win.wait_for_close()

    


if __name__ == "__main__":
    main()