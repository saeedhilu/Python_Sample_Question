# Write a program to find the maximum and minimum   elements in a list of integers
def function(limit):
    value1 = max(limit)
    value2 = min(limit)
    return value1,value2

list1 = [1,2,3,4,667,7,3,6]
value1,value2 = function(list1)
print("This is Your Max value",value1 ,"\n","This is smallest value",value2)