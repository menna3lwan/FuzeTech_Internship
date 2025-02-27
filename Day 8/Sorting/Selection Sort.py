def print_array(arr):

    print("[", end="")

    for i in range(len(arr)):

        print(arr[i], end="")

        if i < len(arr) - 1:
            print(", ", end="")

    print("]")

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


arr = [2, 5, 3, 1, 0,9]
selection_sort(arr)
print("Sorted array:")
print_array(arr)