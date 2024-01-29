    # Write a function to find the second largest number in a list
def function1(value):
    n = len(value)
    for i in range(n-1):
        for j in range(i+1,n):
            if value[i] <    value[j]:
                value[j],value[i] = value[i] , value[j]
    return value
list1 = [12,3,43,342,42244,24,4,24242424242,4]
my_list = function1(list1)
print(my_list[1])