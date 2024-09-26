from line import Point, Line
from window import Window

class Cell():
    def __init__(
        self,
        x1: int = 0,
        y1: int = 0,
        x2: int = 0,
        y2: int = 0,
        window: Window = None
    ) -> None:
        
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._win = window

        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

        self.visited = False
        
    def draw(self) -> None:

        top_left_vertex = Point(self._x1, self._y1)
        top_right_vertex = Point(self._x2, self._y1)
        bottom_left_vertex = Point(self._x1, self._y2)
        bottom_right_vertex = Point(self._x2, self._y2)

        left_wall = Line(top_left_vertex, bottom_left_vertex)
        right_wall = Line(top_right_vertex, bottom_right_vertex)
        top_wall = Line(top_left_vertex, top_right_vertex)
        bottom_wall = Line(bottom_left_vertex, bottom_right_vertex)
        
        if self._win is not None:
            if self.has_left_wall == True:
                left_wall.draw(self._win.canvas, 'black')
            else:
                left_wall.draw(self._win.canvas, 'white')

            if self.has_right_wall == True:
                right_wall.draw(self._win.canvas, 'black')
            else:
                right_wall.draw(self._win.canvas, 'white')

            if self.has_top_wall == True:
                top_wall.draw(self._win.canvas, 'black')
            else:
                top_wall.draw(self._win.canvas, 'white')

            if self.has_bottom_wall == True:
                bottom_wall.draw(self._win.canvas, 'black')
            else:
                bottom_wall.draw(self._win.canvas, 'white')

    def draw_move(self, to_cell, undo=False):

        self_center = Point((self._x1 + self._x2) / 2,
                            (self._y1 + self._y2) / 2)

        to_cell_center = Point((to_cell._x1 + to_cell._x2) / 2,
                               (to_cell._y1 + to_cell._y2) / 2)

        center_to_center = Line(self_center, to_cell_center)

        if undo == False:
            center_to_center.draw(self._win.canvas, 'red')
        else:
            center_to_center.draw(self._win.canvas, 'gray')