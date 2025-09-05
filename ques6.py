rows=6
for i in range(rows):
    dashes= rows - i -1 
    if dashes == 0:
        print(" ")
    else:
        print("*" + "_" * dashes + "*")