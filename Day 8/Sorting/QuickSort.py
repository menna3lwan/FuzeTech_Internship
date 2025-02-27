def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)

        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)


def partition(arr, low, high):
    pivot = arr[high]

    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


# Example usage
original_list = [12, 11, 13, 5, 6, 7]
print("Original list:", original_list)

quicksort(original_list, 0, len(original_list) - 1)
print("Sorted list:", original_list)