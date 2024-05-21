def bubblesort(arr):
    n = len(arr)

    for i in range(n - 1):
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no two elements were swapped by the inner loop, then break

        if not swapped:
            break

    return arr  # Return the sorted array


def main():
    elements = [343, 2, 234, 13, 1, 55, 5]
    result = bubblesort(elements)
    print(result)


if __name__ == "__main__":
    main()
