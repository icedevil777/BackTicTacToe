from tkinter import *
from tkinter import messagebox
import time
import random

# Tkinter parameters
tk = Tk()
app_running = True
tk.title("BackTicTacToe")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)


def on_closing():
    """This function for cool closing app"""
    global app_running
    if messagebox.askokcancel("Are you sure ? ", "Do you want to exit ?"):
        app_running = False
        tk.destroy()


tk.protocol("WM_DELETE_WINDOW", on_closing)

# Game and field parameters
size_canvas_x = 761
size_canvas_y = 761
s_x = 10  # Number of cells
s_y = 10
step_x = size_canvas_x // s_x
step_y = size_canvas_y // s_y
points = [[-1 for i in range(s_x)] for i in range(s_x)]
list_ids = []
type = 0  # Tic or Tac
turn = 1  # Player or computer
canvas = Canvas(tk, width=size_canvas_x, height=size_canvas_y, bd=0,
                highlightthickness=0)
canvas.create_rectangle(0, 0, size_canvas_x, size_canvas_y, fill="white")
canvas.pack()


def draw_table():
    """This function draw all lines"""
    for i in range(0, s_x + 1):
        canvas.create_line(0, i * step_y, size_canvas_x, i * step_y)
    for i in range(0, s_y + 1):
        canvas.create_line(i * step_y, 0, i * step_y, size_canvas_y)


draw_table()


def button_press():
    """New game"""
    global list_ids
    global points
    for i in list_ids:
        canvas.delete(i)
    list_ids = []
    points = [[-1 for i in range(s_x)] for i in range(s_x)]


def button_tic():
    """Play as Tic"""
    global type
    button_press()
    type = 0


def button_tak():
    """Play as Tak"""
    global type
    button_press()
    type = 1


# Buttons
f_bot = Frame(tk)
b_tic = Button(f_bot, bg='yellow', text="Play as Tic", command=button_tic)
b_tok = Button(f_bot, bg='yellow', text="Play as Tak", command=button_tak)
b1 = Button(f_bot, bg='green', text="New game!", command=button_press)
f_bot.pack()
b_tic.pack(side=LEFT, padx=10)
b1.pack(side=LEFT)
b_tok.pack(side=LEFT, padx=10)
tk.update()


def step_player(event):
    """This function add tic or tac from player"""
    global points
    global type
    global turn
    if points[event.x // step_x][event.y // step_y] == -1 or \
            points[event.x // step_x][event.y // step_y] == -2:
        points[event.x // step_x][event.y // step_y] = type
        draw_point(event.x // step_x, event.y // step_y, type)
        if check_winner(type):
            print("Computer is winner!")
            print(points)
            points = [[10 for i in range(s_x)] for i in range(s_x)]
        turn = 0
        type = (int(not type))


save = 0


def step_ai():
    global points
    global type
    global turn
    global save
    t = []  # AI step table
    for y in range(s_y):
        for x in range(s_x):
            t.append([step_x * x + step_x // 2, step_y * y + step_y // 2])

    if turn == 0:
        rand = random.randint(0, 99)
        if points[t[rand][0] // step_x][t[rand][1] // step_y] == -1:
            points[t[rand][0] // step_x][t[rand][1] // step_y] = type
            if check_winner(type) == 0:
                draw_point(t[rand][0] // step_x, t[rand][1] // step_y, type)
                turn = 1
                type = (int(not type))
                # print(f"turn {turn}")
                print(f"type {type}")
            if check_winner(type) == 1:
                points[t[rand][0] // step_x][t[rand][1] // step_y] = -2
                if save < 5:
                    save = save + 1
                    print(f"save {save}")
                else:
                    print("Player is winner!")
                    draw_point(t[rand][0] // step_x,
                               t[rand][1] // step_y, type)
                    save = 0
                    points = [[10 for i in range(s_x)] for i in range(s_x)]


def draw_point(x, y, type):
    """This function draw tic or tac"""
    size = 25
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


def check_winner(who):
    """The function determines who is winner"""
    win = False
    # Horizontal check
    for i in range(0, s_y):
        for j in range(0, s_x // 2 + 1):
            if points[i][j] == who and \
                    points[i][j + 1] == who and \
                    points[i][j + 2] == who and \
                    points[i][j + 3] == who and \
                    points[i][j + 4] == who:
                win = True
    # Vertical check
    for i in range(0, s_x // 2 + 1):
        for j in range(0, s_y):
            if points[i][j] == who and \
                    points[i + 1][j] == who and \
                    points[i + 2][j] == who and \
                    points[i + 3][j] == who and \
                    points[i + 4][j] == who:
                win = True
    # All diagonals check
    for i in range(6):
        if points[i][i] == who and \
                points[i + 1][i + 1] == who and \
                points[i + 2][i + 2] == who and \
                points[i + 3][i + 3] == who and \
                points[i + 4][i + 4] == who:
            win = True
        if points[-1 - i][i + 0] == who and \
                points[-2 - i][i + 1] == who and \
                points[-3 - i][i + 2] == who and \
                points[-4 - i][i + 3] == who and \
                points[-5 - i][i + 4] == who:
            win = True
        if i < 5:
            if points[i + 1][i] == who and \
                    points[i + 2][i + 1] == who and \
                    points[i + 3][i + 2] == who and \
                    points[i + 4][i + 3] == who and \
                    points[i + 5][i + 4] == who:
                win = True
            if points[i][i + 1] == who and \
                    points[i + 1][i + 2] == who and \
                    points[i + 2][i + 3] == who and \
                    points[i + 3][i + 4] == who and \
                    points[i + 4][i + 5] == who:
                win = True
            if points[i][-2 - i] == who and \
                    points[i + 1][-3 - i] == who and \
                    points[i + 2][-4 - i] == who and \
                    points[i + 3][-5 - i] == who and \
                    points[i + 4][-6 - i] == who:
                win = True
            if points[i + 1][-1 - i] == who and \
                    points[i + 2][-2 - i] == who and \
                    points[i + 3][-3 - i] == who and \
                    points[i + 4][-4 - i] == who and \
                    points[i + 5][-5 - i] == who:
                win = True
        if i < 4:
            if points[i + 2][i] == who and \
                    points[i + 3][i + 1] == who and \
                    points[i + 4][i + 2] == who and \
                    points[i + 5][i + 3] == who and \
                    points[i + 6][i + 4] == who:
                win = True
            if points[i][i + 2] == who and \
                    points[i + 1][i + 3] == who and \
                    points[i + 2][i + 4] == who and \
                    points[i + 3][i + 5] == who and \
                    points[i + 4][i + 6] == who:
                win = True
            if points[i][-3 - i] == who and \
                    points[i + 1][-4 - i] == who and \
                    points[i + 2][-5 - i] == who and \
                    points[i + 3][-6 - i] == who and \
                    points[i + 4][-7 - i] == who:
                win = True
            if points[i + 2][-1 - i] == who and \
                    points[i + 3][-2 - i] == who and \
                    points[i + 4][-3 - i] == who and \
                    points[i + 5][-4 - i] == who and \
                    points[i + 6][-5 - i] == who:
                win = True
        if i < 3:
            if points[i + 3][i] == who and \
                    points[i + 4][i + 1] == who and \
                    points[i + 5][i + 2] == who and \
                    points[i + 6][i + 3] == who and \
                    points[i + 7][i + 4] == who:
                win = True
            if points[i][i + 3] == who and \
                    points[i + 1][i + 4] == who and \
                    points[i + 2][i + 5] == who and \
                    points[i + 3][i + 6] == who and \
                    points[i + 4][i + 7] == who:
                win = True
            if points[i][-4 - i] == who and \
                    points[i + 1][-5 - i] == who and \
                    points[i + 2][-6 - i] == who and \
                    points[i + 3][-7 - i] == who and \
                    points[i + 4][-8 - i] == who:
                win = True
            if points[i + 3][-1 - i] == who and \
                    points[i + 4][-2 - i] == who and \
                    points[i + 5][-3 - i] == who and \
                    points[i + 6][-4 - i] == who and \
                    points[i + 7][-5 - i] == who:
                win = True
        if i < 2:
            if points[i + 4][i] == who and \
                    points[i + 5][i + 1] == who and \
                    points[i + 6][i + 2] == who and \
                    points[i + 7][i + 3] == who and \
                    points[i + 8][i + 4] == who:
                win = True
            if points[i][i + 4] == who and \
                    points[i + 1][i + 5] == who and \
                    points[i + 2][i + 6] == who and \
                    points[i + 3][i + 7] == who and \
                    points[i + 4][i + 8] == who:
                win = True
            if points[i][-5 - i] == who and \
                    points[i + 1][-6 - i] == who and \
                    points[i + 2][-7 - i] == who and \
                    points[i + 3][-8 - i] == who and \
                    points[i + 4][-9 - i] == who:
                win = True
            if points[i + 4][-1 - i] == who and \
                    points[i + 5][-2 - i] == who and \
                    points[i + 6][-3 - i] == who and \
                    points[i + 7][-4 - i] == who and \
                    points[i + 8][-5 - i] == who:
                win = True
        if i < 1:
            if points[i + 5][i] == who and \
                    points[i + 6][i + 1] == who and \
                    points[i + 7][i + 2] == who and \
                    points[i + 8][i + 3] == who and \
                    points[i + 9][i + 4] == who:
                win = True
            if points[i][i + 5] == who and \
                    points[i + 1][i + 6] == who and \
                    points[i + 2][i + 7] == who and \
                    points[i + 3][i + 8] == who and \
                    points[i + 4][i + 9] == who:
                win = True
            if points[i][-6 - i] == who and \
                    points[i + 1][-7 - i] == who and \
                    points[i + 2][-8 - i] == who and \
                    points[i + 3][-9 - i] == who and \
                    points[i + 4][-10 - i] == who:
                win = True
            if points[i + 5][-1 - i] == who and \
                    points[i + 6][-2 - i] == who and \
                    points[i + 7][-3 - i] == who and \
                    points[i + 8][-4 - i] == who and \
                    points[i + 9][-5 - i] == who:
                win = True
    return win


# Real time
while app_running:
    if turn == 1:
        canvas.bind_all("<Button-1>", step_player)  # ??????
    elif turn == 0:
        step_ai()

    if app_running:
        tk.update_idletasks()
        tk.update()
        time.sleep(0.00005)
