# Below function returns the sum of a given list of numbers
def sum(n):
    sum = 0
    for i in n:
        sum += i
    return(sum)
# Below function returns the product of a given list of numbers
def pro(n):
    pro = 1
    for i in n:
        pro *= i
    return(pro)   
print("The sum of 1, 2, 3, 4 and 5 =",sum([1,2,3,4,5]))
print("The product of 1, 2, 3, 4 and 5 =",pro([1,2,3,4,5]))
# Hi
