def add(i,j):
    i+=j
    return i
def sub(i,j):
    i-=j
    return i
def mul(i,j):
    i*=j
    return i
def division(i,j):
    i/=j
    return i
def module(i,j):
    i%=j
    return i

def default(i,j):
    print("Incorrect option ")

    
switcher={
    1:add,
    2:sub,
    3:mul,
    4:division,
    5:module
}

def switch(opretion):
    return switcher.get(opretion,default)()

print('''you can perform opretion
      1.add
      2.sub
      3.mul
      4.division
      5.module''')

choice=int(input("Enter your choice : "))
print(switch(choice))