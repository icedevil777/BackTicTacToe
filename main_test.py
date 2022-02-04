from tkinter import *
from tkinter import messagebox
import time
import random

tk = Tk()


app_running = True

size_canvas_x = 761
size_canvas_y = 761


def on_closing():
    """This function for cool closing app"""
    global app_running
    if messagebox.askokcancel("Are you sure ? ", "Do you want to exit ?"):
        app_running = False
        tk.destroy()


tk.protocol("WM_DELETE_WINDOW", on_closing)

tk.title("BackTicTacToe")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=size_canvas_x, height=size_canvas_y, bd=0,
                highlightthickness=0)
canvas.create_rectangle(0, 0, size_canvas_x, size_canvas_y, fill="white")
canvas.pack()
tk.update()

# Field characteristics
s_x = 10  # number of cells
s_y = s_x
step_x = size_canvas_x // s_x
step_y = size_canvas_y // s_y


def draw_table():
    """This function draw all lines"""
    for i in range(0, s_x + 1):
        canvas.create_line(0, i * step_y, size_canvas_x, i * step_y)
    for i in range(0, s_y + 1):
        canvas.create_line(i * step_y, 0, i * step_y, size_canvas_y)


# points = [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]
points = [[-1 for i in range(s_x)] for i in range(s_x)]
print(points)
list_ids = []
draw_table()
type = 0


class Point:
    """ This class for saving points"""

    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)


def draw_point(x, y, type):
    """This function draw tic or tac"""
    size = 25
    color = "black"
    id = 0
    if type == 0:
        color = "red"
        id = canvas.create_oval(x * step_x, y * step_y, x * step_x + step_x,
                                y * step_y + step_y, fill=color)
        id2 = canvas.create_oval(x * step_x + size, y * step_y + size,
                                 x * step_x + step_x - size,
                                 y * step_y + step_y - size, fill="white")
        list_ids.append(id)
        list_ids.append(id2)
    if type == 1:
        color = "blue"
        id = canvas.create_rectangle(x * step_x,
                                     y * step_y + step_y // 2 - step_y // 10,
                                     x * step_x + step_x,
                                     y * step_y + step_y // 2 + step_y // 10,
                                     fill=color)
        id2 = canvas.create_rectangle(x * step_x + step_x // 2 - step_x // 10,
                                      y * step_y,
                                      x * step_x + step_x // 2 + step_x // 10,
                                      y * step_y + step_y, fill=color)
        list_ids.append(id)
        list_ids.append(id2)

    print(type)
    # id = canvas.create_oval(x*step_x, y*step_y, x*step_x+step_x, y*step_y+step_y, fill=color)


def add_to_points(event):
    """This function add tic or tac"""
    print(event.num, event.x, event.y)
    global points
    type = 0
    if event.num == 3:
        type = 1
    if points[event.x // step_x][event.y // step_y] == -1:
        points[event.x // step_x][event.y // step_y] = type
        draw_point(event.x // step_x, event.y // step_y, type)
        if check_winner(type):
            print("winner", type)
            points = [[10 for i in range(s_x)] for i in range(s_x)]
        print(" ".join(map(str, points)))


def button_press():
    """New game"""
    global list_ids
    global points
    print(list_ids)
    for i in list_ids:
        canvas.delete(i)
    list_ids = []
    print(list_ids)
    points = [[-1 for i in range(s_x)] for i in range(s_x)]


def button_tic():
    """Play as Tic"""
    global marker
    button_press()


def button_tok():
    """Play as Tak"""
    button_press()


f_bot = Frame(tk)
b_tic = Button(f_bot, bg='yellow', text="Play as Tic", command=button_tic)
b_tok = Button(f_bot, bg='yellow', text="Play as Tak", command=button_tok)
b1 = Button(f_bot, bg='green', text="New game!", command=button_press)
f_bot.pack()
b_tic.pack(side=LEFT, padx=10)
b1.pack(side=LEFT)
b_tok.pack(side=LEFT, padx=10)


def check_winner(who):
    for j in range(0, s_y):
        win = True
        for i in range(0, s_x):
            if points[j][i] != who:
                win = False
        if win:
            return True
    for j in range(0, s_y):
        win = True
        for i in range(0, s_x):
            if points[i][j] != who:
                win = False
        if win:
            return True

    win = True
    for i in range(0, s_y):
        print(points[i][i])
        if points[i][i] != who:
            win = False
    if win:
        return True


# marker = 0
# if marker == 1:
#     bot = "<Button-1>"
# else:
#     bot = "<Button-3>"
#
while app_running:

    canvas.bind_all("<Button-1>", add_to_points)  # ЛКМ
    # canvas.bind_all("<Button-3>", add_to_points)  # ПКМ

    if app_running:
        tk.update_idletasks()
        tk.update()
    time.sleep(0.005)


