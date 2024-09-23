from typing import Tuple

from line import Point, Line
from window import Window
class Cell():
    def __init__(self,
                x1: int, y1: int, x2: int, y2: int,
                window: Window,
                ) -> None:
        
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
    
    def draw(self, top_left_coordinates: Tuple[int, int], bottom_right_coordinates: Tuple[int, int]) -> None:
        pass