rows = 5
cols = 9

for i in range(rows - 1, -1, -1):  # Start from 4 to 0
    for j in range(cols):
        if j < rows - i - 1 or j >= cols - (rows - i - 1):
            print("*", end=" ")
        else:
            print("_", end=" ")
    print()
