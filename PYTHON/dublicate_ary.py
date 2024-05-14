def Remove(duplicate):
    list=[]
    for i in  duplicate :
        if i not in list :
         list.append(i)
        return list
    
duplicate=[3,4,2,6,5,6,2,4,1]
print(Remove(duplicate))









