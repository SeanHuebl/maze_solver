from tkinter import Canvas

class Point:
    """
    Represents a point in 2D space.

    Attributes:
        x (float): The x-coordinate of the point.
        y (float): The y-coordinate of the point.
    """
    
    def __init__(self, x: float, y: float) -> None:
        """
        Initializes a Point with x and y coordinates.

        Args:
            x (float): The x-coordinate of the point.
            y (float): The y-coordinate of the point.
        """
        self.x = x
        self.y = y

class Line:
    """
    Represents a line segment defined by two points.

    Attributes:
        point_1 (Point): The first point of the line.
        point_2 (Point): The second point of the line.
    """
    
    def __init__(self, point_1: Point, point_2: Point) -> None:
        """
        Initializes a Line with two points.

        Args:
            point_1 (Point): The first point of the line.
            point_2 (Point): The second point of the line.
        """
        self.point_1 = point_1
        self.point_2 = point_2
        
    def draw(self, canvas: Canvas, fill_color: str) -> None:
        """
        Draws the line on a Tkinter canvas.

        Args:
            canvas (Canvas): The canvas on which to draw the line.
            fill_color (str): The color to use for drawing the line.
        """
        canvas.create_line(
            self.point_1.x, self.point_1.y, 
            self.point_2.x, self.point_2.y, 
            fill=fill_color, width=2
        )
