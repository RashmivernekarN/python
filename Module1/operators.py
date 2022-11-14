#Operators in python
a= 7
b= 4
d=a%b 
print(d)
if((a%2)==0):
    print("even")
else:
    print("odd")


# powers
a=4; b=2
result = (a**2)+(b**2)+(2*a*b)
print(result)

a= 13
b=33

print(a<b)
print(a>b)
print(a<=b)
print(a>=b)
print(a!=b)
print(a==b)



a = 34
b = 33
print("Check if", a ,">",b," =", a>b)
print("Check if a < b =", a<b)
print("Check if a is equal to b =", a==b)
print("Check if a is not equal to a = ", a!=b)
print("Check if a is greater then or equal to b =", a>=b)
print("Check if a is less then or equal to a = ", a<=b)

a=True
b=False

#  BO D M A S
print(not(10>20 and 10==10 or 2<3))
    #  F    and   T    or  T
    #        F         or   T
    #                   T
print(a or b)

print(not a)

# a in binary 1010
# b in binary 0100
a=1   
b=2

print(a & b)
print(a | b)
print(~b)
print(bin(a^b))
print("Binary of 10 is: ",bin(a))
print("after rotation:",10<<2,bin(a<<2))