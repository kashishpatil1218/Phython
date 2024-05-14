def average(num):
    if len(num) == 0:
        return None
    else:
        return sum(num) / len(num)

list = [2,3,6,8,4,5,6]
print ("The average of list is ", round(average(list), 2))