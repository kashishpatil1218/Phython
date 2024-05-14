a=int(input("Enter the a :"))
b=int(input("Enter the b :"))

for i in range(max(a,b), 1 + (a*b)):
    if i % a == i % b == 0:
        LCM = i
        break
print("LCM of",a, "and",b, "is", LCM)