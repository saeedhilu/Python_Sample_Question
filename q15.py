# Write a program to find the sum of all prime numbers up to a given limit. 
def functions(limit):
    sum = 0
    if limit<= 1:
        return "Invalid Entry"
    for num in range(2, limit):
        is_prime = True
        for n in range(2,int(num**0.5)+1):
            if num % n == 0 :
                is_prime = False
        if is_prime:
             sum += num 
    return sum
            
value = functions(8)
print(value)
            
    