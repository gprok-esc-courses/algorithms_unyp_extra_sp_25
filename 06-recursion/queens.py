# NOT WORKING, YET

placed = []

def add_queen(placed, row):
    for col in range(8):
        placed.append(col)
        add_queen(placed, row+1)


add_queen(placed, 0)

