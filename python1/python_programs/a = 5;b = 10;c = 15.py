a = 50;b = 50;c = 50
if a>b:
    if a>c:
        print("a=",a,"is big")
    else:
        print("c=",c,"is big")
elif b>c:
    print("b=",b,"is big")
elif a>c:
    print("c=",c,"is big")
else:
    print("all are same")