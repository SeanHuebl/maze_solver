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
        win: Window = None
    ) -> None:
        
        self._x1 = x1
        self._y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self._create_cells()

    def _create_cells(self) -> None:
        self._cells = [[Cell(window=self._win) for _ in range(self.num_rows)] for _ in range(self.num_cols)]

        for i, row in enumerate(self._cells):
            for j, cell in enumerate(row):
                self._draw_cell(i, j)
        return self._cells
    
    def _draw_cell(self, i, j):
        cell = self._cells[i][j]
        cell._x1 = self._x1 + i * self.cell_size_x
        cell._y1 = self._y1 + j * self.cell_size_y
        cell._x2 = self._x1 + (i + 1) * self.cell_size_x
        cell._y2 = self._y1 + (j + 1) * self.cell_size_y

        cell.draw()
        self._animate()
        
    def _animate(self):
        if self._win:
            self._win.redraw()
            sleep(.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)

        self._cells[-1][-1].has_bottom_wall = False
        self._draw_cell(self.num_cols - 1, self.num_rows - 1)