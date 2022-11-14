#nested if
a = 5
b = 10
c = 15
if a>b:
    if a>c:
        print("a value is big")
    else:
        print("c value is big") 
elif b>c:
    print("b value is big")
else:
    print("c value is big") 