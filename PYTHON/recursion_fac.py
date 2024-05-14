def factorial(i):
    if i==0 or  i==1:
     return 1
    else:
       return i*factorial(i-1)

i=int(input("enter num : "))
print("Factorial is :",factorial(i))
