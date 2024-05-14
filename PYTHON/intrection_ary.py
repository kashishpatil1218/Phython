def intersection(a1,a2):
         a3=[value for value in a1 if value in a2]
         return a3
a1=[1,2,3,4,5,9,8,7,6]
a2=[6,7,8,9,4,5,6,1,2,3]      
print(intersection(a1,a2))       