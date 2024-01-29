# Write a function to calculate the sum of all numbers in a list
def function1(value):
    n = len(value)
    sum = 0
    for i in value:
        sum+=i
    return sum
list1 =[1,23,23]
b = function1(list1)
print("sum of all numbers in a list :"+str(b))
# another method using sum
numbers = [1,23,23]
result  = sum(numbers)
print("resul is:"+str(result))


