# Write a program to find the sum of the digits of a given number.
def functions(number):
    sum =0
    numbers = str(number)
    for value in numbers:
            sum+=int(value)
    return sum
value = functions(1240)
print(value)

# 
def functions(numbers):
    sum = 0 
    number = str(numbers)
    for value in number:
        sum += int(value)
    return sum
print(functions(14))