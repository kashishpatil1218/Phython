def sum_d(a):
    if a< 10:
        return a
    else:
        return a%10 + sum_d(a/10)

number = int(input("Enter number: "))

sum = sum_d(number)

print("Sum of digit of number :", sum)