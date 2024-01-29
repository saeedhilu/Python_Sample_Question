# Write a function to calculate the sum of all even numbers between 1 and n.
def functions(value):
    return sum(i for i in range(1, value+1) if i % 2 ==0 )
print(functions(4))