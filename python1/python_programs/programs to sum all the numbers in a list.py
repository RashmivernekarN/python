#programs to sum all the numbers in a list
def sum_list(items):
    sum=0
    for x in items:
        sum+=x
    return sum
print(sum_list([1,2,5]))