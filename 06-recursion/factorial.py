
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return factorial(n-1) * n
    

print(factorial(1000))