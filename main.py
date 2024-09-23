from line import Line, Point
from window import Window



def main() -> None:
    win = Window(800, 600)
    
    # Testing the draw_line method
    point_1 = Point(0,0)
    point_2 = Point(400, 400)
    line = Line(point_1, point_2)
    win.draw_line(line, 'black')

    win.wait_for_close()



if __name__ == "__main__":
    main()