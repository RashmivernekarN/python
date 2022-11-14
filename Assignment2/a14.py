#membership operators
x =24
y = 20
list = [10,20,30,40,50]
if(x in list):
    print("x is present in given list")
else:
    print("x is not present in given list")

if(x not in list):
    print("x is not present in given list")
else:
    print("x is present in given list")

if(x not in list):
    print(x,"x is not present in given list",list)
else:
    print(x,"x is present in given list",list)
