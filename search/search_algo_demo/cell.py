from typing import Self
from graphics import Line, Point, Window

class Cell:
    def __init__(
            self,
            win: Window,
    ):
        self._win = win
        self.has_bottom_wall = True
        self.has_top_wall = True
        self.has_right_wall = True
        self.has_left_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self.visited = False

    def draw(
            self,
            x1: int, y1: int,
            x2: int, y2: int,
    ):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        if self.has_left_wall:
            lw = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(lw)
        else:
            lw = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(lw, self._win.bg)
        if self.has_right_wall:
            rw = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(rw)
        else:
            rw = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(rw, self._win.bg)
        if self.has_top_wall:
            tw = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(tw)
        else:
            tw = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(tw, self._win.bg)
        if self.has_bottom_wall:
            bw = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(bw)
        else:
            bw = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(bw, self._win.bg)

    def draw_move(self, to_cell: Self, undo=False):
        fill_color = "gray" if undo else "red"
        if (
            self._x1 is None or self._x2 is None
            or self._y1 is None or self._y2 is None
            or to_cell._x1 is None or to_cell._x2 is None
            or to_cell._y1 is None or to_cell._y2 is None
        ):
            raise ValueError("Cells should be drawn first")
        cell1_center = Point(
            self._x1 + abs(self._x2 - self._x1)//2,
            self._y1 + abs(self._y2 - self._y1)//2
        )
        cell2_center = Point(
            to_cell._x1 + abs(to_cell._x2 - to_cell._x1)//2,
            to_cell._y1 + abs(to_cell._y2 - to_cell._y1)//2
        )
        line = Line(cell1_center, cell2_center)
        self._win.draw_line(line, fill_color)
