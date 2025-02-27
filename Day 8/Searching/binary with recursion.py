def binary_search(arr, target, left=0, right=None):
 
    if right is None:
        right = len(arr) - 1

    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, right)
    else:
        return binary_search(arr, target, left, mid - 1)

# Example usage
arr = [10, 20, 30, 40, 50]
target = 30
result = binary_search(arr, target)
