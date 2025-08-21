N = int(input("Enter a number: "))
sum_of_digits = sum(int(digit) for digit in str(abs(N)))
print(sum_of_digits)
