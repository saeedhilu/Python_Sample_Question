# Write a function to generate all prime numbers up to a given limit
# def find_prime(limit):
#     primes = []
#     if limit <=2:
#         return False
#     while limit >=2:
#         for i in range(2,limit):
#                 if i % limit ==0:
#                     primes.append(limit[i])
#         return primes
# value = find_prime(17)
# print(value)
def prime_numebrs(limit):
    primes = []
    if limit <=2:
        return "Enter a valid number"
    for num in range(2, limit+1):
        is_prime = True
        for i in range(2,int(num**0.5)+1):
            if num % i ==0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes
value = int(input("Enter The limit"))
result = prime_numebrs(value)
print(result)