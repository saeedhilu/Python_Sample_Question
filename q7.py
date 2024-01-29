# Write a function to remove duplicates from a list 
def fun(value):
    n = len(value)
    count=0
    for i in range(n-1):
        for j in range(i+1,n):
            if value[i]==value[j]:
                value[j] = value[i]
                count+=1 
    return value,count
list1 = [111,2,2,3333,4444,444,44,44,33,33]
f,count = fun(list1)
print(f)
print(count)

# 
def remove_duplicate(value):
    n = len(value)
    unique  = []
    for i in range(n):
        if value[i] not in unique:
            unique.append(value[i])
    return unique
            
list1 = [1,23,3,4,4,45,45,5,5]
sample = remove_duplicate(list1)
print(sample)

 


def fun(value):
    uniquelist = list(set(value))
    return uniquelist
list1 = [1,2,3,3,33,44,55,1,2,3,66,77,77]
a = fun(list1)
print(a)
list2 = [10,20,30,40,[66,77],77]
A = list2[4][0]
print(A)
