# Write a program to find the sum of all the even or odd numbers below a given number.
def functions(number):
    return 'xlThis is Even number',sum(i for i in range(1,number+1) if i % 2 ==0),"This is sum of odd numebers",sum(i for i in range(1,number+1) if i % 2 !=0)
a = list(functions(4))
print((a))
print(type(a))