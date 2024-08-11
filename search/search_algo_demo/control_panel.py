from collections.abc import Callable
from tkinter import LEFT, Button, Entry, Frame, Label
from graphics import Window
from maze import Maze


class ControlPanel:
    def __init__(
        self,
        win: Window,
        maze: Maze
    ):
        self._win = win
        self._maze = maze
        self._algo_frm = self._create_frame()
        self._maze_control_frm = self._create_frame()
        self._solve_dfs_btn = self._add_button(
            self._algo_frm,
            "Solve with DFS algorithm",
            maze.solve,
            pack_options={
                "ipadx": 20,
                "ipady": 5,
            }
        )
        self._solve_bfs_btn = self._add_button(
            self._algo_frm,
            "Solve with BFS algorithm",
            maze.solve_bfs,
            pack_options={
                "ipadx": 20,
                "ipady": 5,
            }
        )
        self._solve_a_star_btn = self._add_button(
            self._algo_frm,
            "Solve with A* search algorithm",
            maze.solve_a_star,
            pack_options={
                "ipadx": 3,
                "ipady": 5,
            }
        )
        self._rows_input, self._cols_input = self._add_size_input(
            self._maze_control_frm,
            pack_options={
                "padx": 5,
                "pady": 5,
            }
        )
        self._add_button(
            self._maze_control_frm,
            "New Maze",
            self._create_new_maze,
            fg="#333333",
            pack_options={
                "side": LEFT,
                "ipadx": 30,
                "ipady": 5,
            }
        )

    def _create_frame(self):
        return self._win.add_frame(
            height=100,
            width=self._win.width/2,
            padx=10,
            pady=10,
            pack_options={
                "side": LEFT
            }
        )

    def _add_button(self, parent, text: str, command: Callable, **kwargs):
        pack_options = kwargs.pop("pack_options", {})
        bg = kwargs.pop("bg") if "bg" in kwargs else self._win.bg
        btn = Button(
            parent,
            text=text,
            command=command,
            bg=bg,
            **kwargs
        )
        btn.pack(
            **pack_options
        )
        return btn

    def _add_size_input(self, parent, **kwargs):
        pack_options = kwargs.pop("pack_options", {})
        bg = kwargs.pop("bg") if "bg" in kwargs else self._win.bg

        frm = Frame(parent, bg=bg)
        frm.pack(fill='x', expand=1)

        lbl = Label(
            frm,
            text="size",
            font=("Sans-serif", 18, "italic"),
            bg=bg,
        )
        lbl.pack(side=LEFT, ipadx=5, ipady=10)
        row = Entry(frm, bg=bg, width=3, **kwargs)
        row.pack(side=LEFT, **pack_options)

        lbl2 = Label(
            frm,
            text="x",
            font=("Sans-serif", 18),
            bg=bg,
        )
        lbl2.pack(side=LEFT, ipadx=5, ipady=10)
        column = Entry(frm, bg=bg, width=3, **kwargs)
        column.pack(side=LEFT, **pack_options)

        row.insert(0, '12')
        column.insert(0, '12')
        return row, column

    def _create_new_maze(self):
        self._win.clear_canvas()
        margin = 25
        num_rows = int(self._rows_input.get())
        num_cols = int(self._cols_input.get())
        cell_size_x = (self._win.width - margin*2)//num_cols
        cell_size_y = (self._win.height - margin*2)//num_rows
        maze = Maze(
            margin, margin,
            num_rows, num_cols,
            cell_size_x, cell_size_y,
            self._win,
        )
        self._solve_dfs_btn.configure(command=maze.solve)
        self._solve_bfs_btn.configure(command=maze.solve_bfs)
        self._solve_a_star_btn.configure(command=maze.solve_a_star)
