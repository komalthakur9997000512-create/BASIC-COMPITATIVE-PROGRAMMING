
def sum_of_even_numbers(A):
    total = 0
    for i in range(2, A + 1, 2): 
        total += i
    return total


A = 5
print(sum_of_even_numbers(A)) 