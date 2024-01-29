# A program to print the Fibonacci series
def functions(value):
    new_Fibanaci = [0,1]
    while len(new_Fibanaci) < value:
        sum =new_Fibanaci[-1]+new_Fibanaci[-2]
        new_Fibanaci.append(sum)
    return new_Fibanaci

value = functions(20)
print(value)
    #
def functions(value):
    new_Fibanaci = [0,1]
    for _ in range(value-2):    
        sum =new_Fibanaci[-1]+new_Fibanaci[-2]
        new_Fibanaci.append(sum)
    return new_Fibanaci

value = functions(20)
print(value)   
        
#  another methiod
def functions(limit):
    result = []
    a , b = 0 , 1
    while a <= limit:
       result.append(a)
       a , b = b , a + b
    return result
value = functions(10)     
print(value)
        