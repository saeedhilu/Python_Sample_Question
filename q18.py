# Write a program to find the union of two lists of integers.
def functions(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    
    set3 = set1.union(set2)
    return set(set3)
list1 = [1,2,3,4,5,6,7,8,8]
list2 = [1,2,3,4,5,6,7,8,8,9,9,9,9,9,9]

value = functions(list1,list2)
print(value)
#
def functions(v1,v2):
    set1 = set(v1)  
    set2 = set(v2)
    set3 = set1.union(set2)
    return set3
list1 = [1,2,3,4,5,6,7,8,8]
list2 = [1,2,3,4,5,6,7,8,8,9,9,9,9,9,9]
print(functions(list1,list2))