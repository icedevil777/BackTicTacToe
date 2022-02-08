def check_winner(who, s_xy, points):
    """The function determines who is winner"""
    win = False
    for i in range(s_xy):
        try:
            if points[i][i] == who and \
                    points[i + 1][i + 1] == who and \
                    points[i + 2][i + 2] == who and \
                    points[i + 3][i + 3] == who and \
                    points[i + 4][i + 4] == who or \
                    points[-1 - i][i + 0] == who and \
                    points[-2 - i][i + 1] == who and \
                    points[-3 - i][i + 2] == who and \
                    points[-4 - i][i + 3] == who and \
                    points[-5 - i][i + 4] == who or \
                    points[i + 1][i] == who and \
                    points[i + 2][i + 1] == who and \
                    points[i + 3][i + 2] == who and \
                    points[i + 4][i + 3] == who and \
                    points[i + 5][i + 4] == who or \
                    points[i][i + 1] == who and \
                    points[i + 1][i + 2] == who and \
                    points[i + 2][i + 3] == who and \
                    points[i + 3][i + 4] == who and \
                    points[i + 4][i + 5] == who or \
                    points[i][-2 - i] == who and \
                    points[i + 1][-3 - i] == who and \
                    points[i + 2][-4 - i] == who and \
                    points[i + 3][-5 - i] == who and \
                    points[i + 4][-6 - i] == who or \
                    points[i + 1][-1 - i] == who and \
                    points[i + 2][-2 - i] == who and \
                    points[i + 3][-3 - i] == who and \
                    points[i + 4][-4 - i] == who and \
                    points[i + 5][-5 - i] == who or \
                    points[i + 2][i] == who and \
                    points[i + 3][i + 1] == who and \
                    points[i + 4][i + 2] == who and \
                    points[i + 5][i + 3] == who and \
                    points[i + 6][i + 4] == who or \
                    points[i][i + 2] == who and \
                    points[i + 1][i + 3] == who and \
                    points[i + 2][i + 4] == who and \
                    points[i + 3][i + 5] == who and \
                    points[i + 4][i + 6] == who or \
                    points[i][-3 - i] == who and \
                    points[i + 1][-4 - i] == who and \
                    points[i + 2][-5 - i] == who and \
                    points[i + 3][-6 - i] == who and \
                    points[i + 4][-7 - i] == who or \
                    points[i + 2][-1 - i] == who and \
                    points[i + 3][-2 - i] == who and \
                    points[i + 4][-3 - i] == who and \
                    points[i + 5][-4 - i] == who and \
                    points[i + 6][-5 - i] == who or \
                    points[i + 3][i] == who and \
                    points[i + 4][i + 1] == who and \
                    points[i + 5][i + 2] == who and \
                    points[i + 6][i + 3] == who and \
                    points[i + 7][i + 4] == who or \
                    points[i][i + 3] == who and \
                    points[i + 1][i + 4] == who and \
                    points[i + 2][i + 5] == who and \
                    points[i + 3][i + 6] == who and \
                    points[i + 4][i + 7] == who or \
                    points[i][-4 - i] == who and \
                    points[i + 1][-5 - i] == who and \
                    points[i + 2][-6 - i] == who and \
                    points[i + 3][-7 - i] == who and \
                    points[i + 4][-8 - i] == who or \
                    points[i + 3][-1 - i] == who and \
                    points[i + 4][-2 - i] == who and \
                    points[i + 5][-3 - i] == who and \
                    points[i + 6][-4 - i] == who and \
                    points[i + 7][-5 - i] == who or \
                    points[i + 4][i] == who and \
                    points[i + 5][i + 1] == who and \
                    points[i + 6][i + 2] == who and \
                    points[i + 7][i + 3] == who and \
                    points[i + 8][i + 4] == who or \
                    points[i][i + 4] == who and \
                    points[i + 1][i + 5] == who and \
                    points[i + 2][i + 6] == who and \
                    points[i + 3][i + 7] == who and \
                    points[i + 4][i + 8] == who or \
                    points[i][-5 - i] == who and \
                    points[i + 1][-6 - i] == who and \
                    points[i + 2][-7 - i] == who and \
                    points[i + 3][-8 - i] == who and \
                    points[i + 4][-9 - i] == who or \
                    points[i + 4][-1 - i] == who and \
                    points[i + 5][-2 - i] == who and \
                    points[i + 6][-3 - i] == who and \
                    points[i + 7][-4 - i] == who and \
                    points[i + 8][-5 - i] == who or \
                    points[i + 5][i] == who and \
                    points[i + 6][i + 1] == who and \
                    points[i + 7][i + 2] == who and \
                    points[i + 8][i + 3] == who and \
                    points[i + 9][i + 4] == who or \
                    points[i][i + 5] == who and \
                    points[i + 1][i + 6] == who and \
                    points[i + 2][i + 7] == who and \
                    points[i + 3][i + 8] == who and \
                    points[i + 4][i + 9] == who or \
                    points[i][-6 - i] == who and \
                    points[i + 1][-7 - i] == who and \
                    points[i + 2][-8 - i] == who and \
                    points[i + 3][-9 - i] == who and \
                    points[i + 4][-10 - i] == who or \
                    points[i + 5][-1 - i] == who and \
                    points[i + 6][-2 - i] == who and \
                    points[i + 7][-3 - i] == who and \
                    points[i + 8][-4 - i] == who and \
                    points[i + 9][-5 - i] == who:
                win = True
        except:
            continue
        for i in range(s_xy):
            for j in range(s_xy):
                try:
                    if points[i][j + 0] == who and \
                            points[i][j + 1] == who and \
                            points[i][j + 2] == who and \
                            points[i][j + 3] == who and \
                            points[i][j + 4] == who or \
                            points[j + 0][i] == who and \
                            points[j + 1][i] == who and \
                            points[j + 2][i] == who and \
                            points[j + 3][i] == who and \
                            points[j + 4][i] == who:
                        win = True
                except:
                    continue
    return win
