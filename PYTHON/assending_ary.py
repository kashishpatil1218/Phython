
array=[10,2,50,3,20]

a=0

print("Element of array : ")
for i in range(0,len(array)):
    print(array[i],end=' ')

for i in range(0,len(array)):
    for j in range(i+1,len(array)):
        if(array[i]>array[j]):
            a=array[i]
            array[i]=array[j]
            array[j]=a
        print()

print("Element of ascending order : ")

for i in range(0,len(array)):
    print(array[i],end=' ')