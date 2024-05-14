def n_sum(i):
    sum=0
    count=1

    while count<=i:
        sum=sum+count
        count+1

        return sum
    
i=int (input("enter value :"))

total=n_sum(i)
print("natural num sum :",total)


