rows = 5
cols = 9

for i in range(rows):
    for j in range(cols):
        if j < rows - i - 1 or j >= cols - (rows - i - 1):
            print("*", end=" ")
        else:
            print("_", end=" ")
    print()


