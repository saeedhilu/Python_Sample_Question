# Write a function to sort a input_list in ascending order using for loop
# input_list1 = [1,2,3,34,56,787,89]
# input_list1.sort(-1)
# input_list1 = [1, 2, 3, 34, 56, 787, 89]
# input_list1.sort(reverse=True)

# print("Sorted input_List (Descending):", input_list1)
# input_list1 = [1, 2, 3, 34, 56, 787, 89]
# sorted_input_list = sorted(input_list1)

# print("Original input_List:", input_list1)
# print("Sorted input_List (Ascending):", sorted_input_list)

def fun(input):
    n = len(input)
    
    for i in range(n-1):
        for j in range(i+1,n):
            if input[j]<input[i]:
              input[i],   input[j]  = input[j],input[i] 
    return  input
list1 = [1, 2, 3, 34, 56, 787, 89,1]
sorted_list =  fun(list1)
print(sorted_list)
# Write a function to sort a input_list in descending order using for loop
def descending(value):
    n = len(value)
    for i in range(n-1):
        for j in range(i+1,n):
            if value[i] < value[j]:
                value[j], value[i] = value[i], value[j]
    return value
list1 = [12,3,43,342,42244,24,4,24242424242,4]
new_list = descending(list1)
print(new_list) 