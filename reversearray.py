def reversearray(arr):
    if not arr:
        return 0

    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left = +1
        right -= 1

    return arr


def main():
    arr = [1, 5, 53, 2, 5]
    result = reversearray(arr)
    print(result)


main()
