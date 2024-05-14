a=int(input("enter the a :"))

reverse=0

while a>0:
    temp=a%10
    reverse=(reverse*10)+temp
    a=a//10

print("reverse number is : ",reverse)
