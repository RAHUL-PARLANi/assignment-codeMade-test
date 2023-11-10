print('Hello, world!')
print('Hello, world!')
print('Hello, world!')
print('Hello, world!')
print('Hello, world!')
print('Hello, world!')
def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index  # Return the index if the target is found
    return -1  # Return -1 if the target is not found

# Example usage:
my_list = [4, 2, 7, 1, 9, 5]
element_to_find = 7

result = linear_search(my_list, element_to_find)

if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found in the list")
