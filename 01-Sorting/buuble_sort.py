
data = [35, 12, 4, 37, 81, 14, 23, 1, 19]

for stop in range(len(data)-1, 0, -1):
    for i in range(stop):
        if data[i] > data[i+1]:
            data[i], data[i+1] = data[i+1], data[i]

print(data)