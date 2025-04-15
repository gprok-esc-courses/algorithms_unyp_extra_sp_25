
def hanoi(n, source, dest, aux):
    if n > 0:
        hanoi(n - 1, source, aux, dest)
        print("move", n, source, dest)
        hanoi(n - 1, aux, dest, source)


hanoi(3, "A", "C", "B")