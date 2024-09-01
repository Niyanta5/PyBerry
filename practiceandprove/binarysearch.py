def binarySearch(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            left = mid + 1

        elif arr[mid] > target:
            left = mid - 1

    return -1


def main():
    sortedarray = [1, 3, 5, 7, 9, 12]
    result = binarySearch(sortedarray, 9)
    print(result)


if __name__ == "__main__":
    main()

