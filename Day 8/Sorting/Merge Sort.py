def merge(array, left, mid, right):
    left_size = mid - left + 1
    right_size = right - mid

    left_array = [0] * left_size
    right_array = [0] * right_size

    for i in range(left_size):
        left_array[i] = array[left + i]
    for j in range(right_size):
        right_array[j] = array[mid + 1 + j]

    i = 0
    j = 0
    k = left

    while i < left_size and j < right_size:
        if left_array[i] <= right_array[j]:
            array[k] = left_array[i]
            i += 1
        else:
            array[k] = right_array[j]
            j += 1
        k += 1

    while i < left_size:
        array[k] = left_array[i]
        i += 1
        k += 1

    while j < right_size:
        array[k] = right_array[j]
        j += 1
        k += 1

def merge_sort(array, left, right):
    if left < right:
        mid = (left + right) // 2

        merge_sort(array, left, mid)

        merge_sort(array, mid + 1, right)

        # Merge the sorted halves
        merge(array, left, mid, right)

def print_array(array):
    for element in array:
        print(element, end=" ")
    print()

if __name__ == "__main__":
    array = [12, 11, 13, 5, 6, 7]
    print("Given array is")
    print_array(array)

    merge_sort(array, 0, len(array) - 1)

    print("\nSorted array is")
    print_array(array)