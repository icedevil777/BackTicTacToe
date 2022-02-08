def draw_table(s_xy, step, size_canvas, canvas):
    """This function draw all lines"""
    for i in range(0, s_xy + 1):
        canvas.create_line(0, i * step, size_canvas, i * step)
    for i in range(0, s_xy + 1):
        canvas.create_line(i * step, 0, i * step, size_canvas)