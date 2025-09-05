rows = 5
num = 1  # Starting odd number

# Loop to print the pattern
for i in range(1, rows + 1):
    pattern = ""
    current_odd = 1
    for j in range(1, i + 1):
        if j % 2 == 0:
            pattern += "*"
        else:
            pattern += str(current_odd)
            current_odd += 2
    print(pattern)