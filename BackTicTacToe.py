from tkinter import *
from tkinter import messagebox
import time
import random
from check_winner import *

# Tkinter parameters
tk = Tk()
app_running = True
tk.title("BackTicTacToe")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
# Game and field parameters
size_canvas = 661
s_xy = 10  # Number of cells
save = 0
step = size_canvas // s_xy
points = [[-1 for i in range(s_xy)] for i in range(s_xy)]
list_ids = []
type = 0  # Tic or Tac
turn = 1  # Player or computer
AI_table = []  # AI step table
for y in range(s_xy):
    for x in range(s_xy):
        AI_table.append([step * x + step // 2, step * y + step // 2])
canvas = Canvas(tk, width=size_canvas, height=size_canvas, bd=0,
                highlightthickness=0)
canvas.create_rectangle(0, 0, size_canvas, size_canvas, fill="white")
canvas.pack()


def on_closing():
    """This function for cool closing app"""
    global app_running
    if messagebox.askokcancel("Are you sure ? ", "Do you want to exit ?"):
        app_running = False
        tk.destroy()


tk.protocol("WM_DELETE_WINDOW", on_closing)


def draw_table():
    """This function draw all lines"""
    for i in range(0, s_xy + 1):
        canvas.create_line(0, i * step, size_canvas, i * step)
    for i in range(0, s_xy + 1):
        canvas.create_line(i * step, 0, i * step, size_canvas)


def button_press():
    """New game"""
    global list_ids
    global points
    for i in list_ids:
        canvas.delete(i)
    list_ids = []
    points = [[-1 for i in range(s_xy)] for i in range(s_xy)]


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
    if points[event.x // step][event.y // step] == -1 or \
            points[event.x // step][event.y // step] == -2:
        points[event.x // step][event.y // step] = type
        draw_point(event.x // step, event.y // step, type)
        if check_winner(type, s_xy, points):
            print("Computer is winner!")
            print("Computer is winner!")
            messagebox.showinfo("Game over", "Computer is winner!")

            # print(points)
            points = [[10 for i in range(s_xy)] for i in range(s_xy)]
            button_press()
        turn = 0
        type = (int(not type))


def step_ai():
    global points
    global type
    global turn
    global save
    if turn == 0:
        rand = random.randint(0, 99)
        if points[AI_table[rand][0] // step][AI_table[rand][1] // step] == -1:
            points[AI_table[rand][0] // step][AI_table[rand][1] // step] = type
            if check_winner(type, s_xy, points) == 0:
                draw_point(AI_table[rand][0] // step,
                           AI_table[rand][1] // step, type)
                turn = 1
                type = (int(not type))
                # print(f"turn {turn}")
                # print(f"type {type}")
            if check_winner(type, s_xy, points) == 1:
                points[AI_table[rand][0] \
                       // step][AI_table[rand][1] // step] = -2
                if save < 3:
                    save = save + 1
                    # print(f"save {save}")
                else:
                    print("Player is winner!")

                    messagebox.showinfo("Game over",
                                        "Player is winner!")
                    draw_point(AI_table[rand][0] // step,
                               AI_table[rand][1] // step, type)
                    save = 0
                    points = [[10 for i in range(s_xy)] for i in range(s_xy)]
                    button_press()


def draw_point(x, y, type):
    """This function draw tic or tac"""
    size = 25
    id = 0
    if type == 0:
        color = "red"
        id = canvas.create_oval(x * step, y * step, x * step + step,
                                y * step + step, fill=color)
        id2 = canvas.create_oval(x * step + size, y * step + size,
                                 x * step + step - size,
                                 y * step + step - size, fill="white")
        list_ids.append(id)
        list_ids.append(id2)
    if type == 1:
        color = "blue"
        id = canvas.create_rectangle(x * step,
                                     y * step + step // 2 - step // 10,
                                     x * step + step,
                                     y * step + step // 2 + step // 10,
                                     fill=color)
        id2 = canvas.create_rectangle(x * step + step // 2 - step // 10,
                                      y * step,
                                      x * step + step // 2 + step // 10,
                                      y * step + step, fill=color)
        list_ids.append(id)
        list_ids.append(id2)


draw_table()

# Real time
while app_running:
    if turn == 1:
        canvas.bind("<Button-1>", step_player)  # ЛКМ
    elif turn == 0:
        step_ai()

    if app_running:
        tk.update_idletasks()
        tk.update()
        time.sleep(0.00005)
