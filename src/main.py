from cell import Cell
from line import Line, Point
from maze import Maze
from window import Window



def main() -> None:
    win = Window(800, 600)
    maze = Maze(0, 0, 10, 10, 25, 25, win)
    maze._break_entrance_and_exit()
    maze._break_walls_r(0, 0)
    win.wait_for_close()

    


if __name__ == "__main__":
    main()