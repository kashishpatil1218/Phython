num1=int(input("enter the num :"))
sum=0

num2=num1

while num2>0:
    total=num2%10
    sum+=total**3
    num2//=10

if num1==sum:
        print("This num is Armstrong")
else:
      print("This num is not Armstrong ")