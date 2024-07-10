def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


sorted_array = [2, 5, 7, 12, 18, 20, 27]
target = 12
print(binary_search(sorted_array, target))
