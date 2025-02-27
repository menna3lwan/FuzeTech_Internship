def linear_search(arr, target):

    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return -1

# Example usage
arr = [10, 20, 30, 40, 50]
target = 30
result = linear_search(arr, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")