
#write a program to grnerate the fibonacci series

n=int(input("Enter the num : "))
num1=0
num2=1
i=0
if n<=0:
    print("e20nter postive num")
elif n==1:
    print("Fibonacci series : ",n)
    print(num1)
else:
    print("Fibonacci series : ")


while i<n:
    print(num1)
    num3=num1+num2
    num1=num2
    num2=num3
    i+=1