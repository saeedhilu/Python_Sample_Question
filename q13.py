# Write a function to check if a given number is an Armstrong number
def armstrong (number):
    value1 = str(number)
    n = len(value1)
    var = 0
    for i in value1:
        var += int(i)**n 
    return var == number
fu = armstrong (7)
print(fu)  



def armstrong (number):
    value1 = str(number)
    n = len(value1)
    var = sum(int(digit)**n for digit in value1)
    return var == number
fu = armstrong (9)
print(fu)
    
    
def armstrong(number):
    value1 = str(number)
    n = len(value1)
    sum = 0
    for i in value1:
        sum+= int(i) ** n
    return sum == number
fu = armstrong(153)
print(fu)
