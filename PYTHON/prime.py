a=int(input("enter the a :"))
i=2
temp=0

while i<=a/2:
    if(a%i==0):
        temp=0
        i+=1
        break


    if a==1:
        print("1 is neither prime nor composite")
    else :  
        if temp==0:
            print(a,"is prime number")
        else:
            print(a,"This is not prime number")

