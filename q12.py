# # Write a function to check given string is palindrome or not
# a = " saeeed ,,,fsasf sfasfsfs TTTTffg dgdg"
# new = ''.join(a.split()).lower()
# print(new)

def pallindromic(value):
    return value == value[::-1]
value = input("Enter String Vsalue")
result = pallindromic(value)
if result:
    print(f"This is pallindromic:{value}")
else:
    print(f"This not pallindromic:{value}")
# 
def pallindromic(value):
    if value == value[::-1]:
        return True
    else:
        return False
value = "ABABA"
inputt = pallindromic(value)
print(inputt)