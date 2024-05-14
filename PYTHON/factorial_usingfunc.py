a=int(input("enter the a :"))
factorail=1
if a<0:
     print("Factorial does not exist in negative value")
elif a==0:
     print("The factorial of 0 is 1")
else:
     for i in range(1,a+1):
          factorail=factorail*i

          print("factorail is :",factorail)