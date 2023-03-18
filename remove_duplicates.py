def remove_duplicates(arr):
    unique_arr = []
    removed_elements = []
    for element in arr:
        if element not in unique_arr:
            unique_arr.append(element)
        else:
            removed_elements.append(element)
    return unique_arr, removed_elements

# Test the function
arr = [1, 2, 2, 3, 4, 4, 5]
unique_arr, removed_elements = remove_duplicates(arr)
print("Original array:", arr)
print("Unique array:", unique_arr)
print("Removed elements:", removed_elements)