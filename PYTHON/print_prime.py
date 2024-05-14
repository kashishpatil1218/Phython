a=int(input("enter a :"))
b=int(input("enter b :"))

print("Prime number :")

for i in range(a,b+1):
    if a>1:
        for j in range(2,i):
            if i%j==0:
                break
            else:
                print(i)