from tkinter import *
from tkinter import messagebox
import time
import random

tk = Tk()
app_running = True

size_canvas_x = 768
size_canvas_y = 768


def on_closing():
    """ This function for cool closing app"""
    global app_running
    if messagebox.askokcancel("Quit", "Do you want to quit ?"):
        app_running = False
        tk.destroy()


tk.protocol("WM_DELETE_WINDOW", on_closing)
# Window Options
tk.title("TicTacToe")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
convas = Canvas(tk, width=size_canvas_x, height=size_canvas_y, bd=0,
                highlightthickness=0)
convas.pack()
tk.update()

s_x = 3
s_y = 3
step_x = size_canvas_x // s_x
step_y = size_canvas_y // s_y


def draw_table():
    """ This function is drawing lines"""
    for i in range(0, s_x + 1):
        convas.create_line(0, i * step_y, size_canvas_x, i * step_y)
    for i in range(0, s_y + 1):
        convas.create_line(i * step_y, 0, i * step_y, size_canvas_y)


points = []
draw_table()


class Point:
    """ This class for saving points"""

    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)


def draw_point(x, y, type):
    size = 25
    color = "black"
    id = 0
    if type == 0:
        color = "red"
        id = convas.create_oval(x * step_x, y * step_y, x * step_x + step_x,
                                y * step_y + step_y, fill=color)
        id2 = convas.create_oval(x * step_x + size, y * step_y + size,
                                 x * step_x + step_x - size,
                                 y * step_y + step_y - size, fill="white")
    if type == 1:
        color = "blue"

    # id = convas.create_oval(x*step_x, y*step_y, x*step_x + step_x,
    #                         y*step_y + step_y, fill=color)



def add_to_points(event):
    print(event.num, event.x, event.y)
    type = 0
    if event.num == 3:
        type = 1
    points.append(Point(event.x // step_x, event.y // step_y, type))
    draw_point(event.x // step_x, event.y // step_y, type)
    print(" ".join(map(str, points)))


convas.bind_all("<Button-1>", add_to_points)  # left
convas.bind_all("<Button-3>", add_to_points)  # right

# For the app to work
while app_running:
    if app_running:
        tk.update_idletasks()
        tk.update()
    time.sleep(0.005)
