def sum_of_odd_numbers(A):
    total = 0
    for i in range(1, A + 1, 2): 
        total += i
    return total

A = 6
print(sum_of_odd_numbers(A))  