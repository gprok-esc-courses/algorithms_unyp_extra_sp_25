# NOT WORKING, YET

# Formula to find if attacked
# abs(placed[row] - cur_col) == abs(row - cur-row)

placed = []

def add_queen(placed, row):
    for col in range(8):
        placed.append(col)
        add_queen(placed, row+1)


add_queen(placed, 0)

