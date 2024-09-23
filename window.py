from tkinter import Tk, BOTH, Canvas

from line import Line

class Window():
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self.__root_widget = Tk()
        self.__root_widget.title = 'root'
        self.__root_widget.geometry(f"{width}x{height}")
        self.__root_widget.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = Canvas(width=self.width, height=self.height)
        self.canvas.pack()
        self.running = False
    
    def redraw(self) -> None:
        self.__root_widget.update_idletasks()
        self.__root_widget.update()

    def wait_for_close(self) -> None:
        self.running = True

        while self.running == True:
            self.redraw()
    
    def close(self) -> None:
        self.running = False

    def draw_line(self, line: Line, fill_color: str) -> None:
        line.draw(self.canvas, fill_color)