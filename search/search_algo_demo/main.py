from control_panel import ControlPanel
from graphics import Window
from maze import Maze


def main():
    window_width = 800
    window_height = 600
    win = Window(
        width=window_width,
        height=window_height,
        bg="black", color="white"
    )

    win.add_title("How to be Late to Class 101")

    maze = init_maze(win)

    ControlPanel(win, maze)

    win.wait_for_close()


def init_maze(win: Window):
    margin = 25
    num_rows = 12
    num_cols = 12
    cell_size_x = (win.width - margin*2)//num_cols
    cell_size_y = (win.height - margin*2)//num_rows

    return Maze(
        margin, margin,
        num_rows, num_cols,
        cell_size_x, cell_size_y,
        win,
    )

if __name__ == "__main__":
    main()