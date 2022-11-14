#
a = 10
b = 20

list1 = ['alpha','beta','gama','delta']
list2 = ['d','c','b','a']
list3 = [10,20,30,40,50]

print(min(list1))
print(set(list1))
print(tuple(list2))

zipped = zip(list1,list2)
print(dict(zipped))

list1.append(a)
print(list1)

list1.append(list2)
print(list1) 