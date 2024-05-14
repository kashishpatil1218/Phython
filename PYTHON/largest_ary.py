array=[1,20,50,2,3,100]

maxNumber=array[0]

for i in range(len(array)):
    if array[i]>maxNumber:
     maxNumber=array[i]


print("Maximum number : ",maxNumber)