from cell import Cell
from line import Line, Point
from window import Window



def main() -> None:
    win = Window(800, 600)
    
    # Testing the draw_line method
    point_1 = Point(0,0)
    point_2 = Point(400, 400)
    line = Line(point_1, point_2)
    win.draw_line(line, 'black')

    # Testing drawing a full cell
    cell = Cell(50, 50, 75, 75, win.canvas)
    cell.draw()
    
    # Testing drawing cells without walls
    cell2 = Cell(15, 15, 30, 30, win.canvas)
    cell2.has_bottom_wall = False
    cell2.has_top_wall = False
    cell2.draw()
    
    cell3 = Cell(100, 100, 125, 125, win.canvas)
    cell3.has_left_wall = False
    cell3.has_right_wall = False
    cell3.draw()
    
    win.wait_for_close()

    


if __name__ == "__main__":
    main()