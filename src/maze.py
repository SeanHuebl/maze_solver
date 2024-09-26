import random
from time import sleep

from cell import Cell
from window import Window


class Maze():
    def __init__(
        self,
        x1: int,
        y1: int,
        num_rows: int,
        num_cols: int,
        cell_size_x: int,
        cell_size_y: int,
        win: Window = None,
        seed: int = None
    ) -> None:
        
        self._x1 = x1
        self._y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self._create_cells()
        if seed is not None:
            random.seed(seed)

    def _create_cells(self) -> None:
        self._cells = [[Cell(window=self._win) for _ in range(self.num_rows)] for _ in range(self.num_cols)]

        for i, row in enumerate(self._cells):
            for j, cell in enumerate(row):
                self._draw_cell(i, j)
        return self._cells
    
    def _draw_cell(self, i: int, j: int) -> None:
        cell = self._cells[i][j]
        cell._x1 = self._x1 + i * self.cell_size_x
        cell._y1 = self._y1 + j * self.cell_size_y
        cell._x2 = self._x1 + (i + 1) * self.cell_size_x
        cell._y2 = self._y1 + (j + 1) * self.cell_size_y

        cell.draw()
        self._animate()
        
    def _animate(self) -> None:
        if self._win:
            self._win.redraw()
            sleep(.05)

    def _break_entrance_and_exit(self) -> None:
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)

        self._cells[-1][-1].has_bottom_wall = False
        self._draw_cell(self.num_cols - 1, self.num_rows - 1)

    def _break_walls_r(self, i: int, j: int) -> None:
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            right = (i + 1, j)
            left = (i - 1, j)
            top = (i, j - 1)
            bottom = (i, j + 1)

            directions = (right, left, top, bottom)

            for direction in directions:
                if direction[0] < 0 or direction[1] < 0:
                    continue
                if direction[0] > len(self._cells):
                    continue
                if direction[1] > len(self._cells[0]):
                    continue
                if self._cells[direction[0]][direction[1]].visited == False:
                    if direction not in to_visit:
                        to_visit.append(direction)
            if len(to_visit) == 0:
                return
            else:
                move = random.randrange(0, len(to_visit))
                direction = to_visit[move]
                cell = self._cells[i][j]
                if  direction == right:
                    cell.has_right_wall = False
                elif direction == left:
                    cell.has_left_wall = False
                elif direction == top:
                    cell.has_top_wall = False
                else:
                    cell.has_bottom_wall = False
                cell.draw()

                i, j = to_visit[move]
                self._break_walls_r(i, j)