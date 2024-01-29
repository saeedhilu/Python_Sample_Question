# Write a program to count the number of vowels in a given string.
def functions(value):
    count = 0
    value1 = value.lower()
    vowels = ["a","i","e","o","u"]
    for i in value1:
        if i in vowels:
            count+=1
    return count
        
print(functions("HEEllo iam here"))
# 
def functions(value):
    count = 0
    value1 = value.lower() # hello iam here
    vowels = ["a","i","e","o","u"]
    for i in value1:
        if i in vowels:
            count+=1
    return count
        
print(functions("HEEllo iam here"))
