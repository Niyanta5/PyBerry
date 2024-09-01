def reversearraywithloop(arr):
    reversed_arr = []

    for i in arr:
        reversed_arr.insert(0, i)

    return reversed_arr


def main():
    arr = [1, 53, 63, 2, 5]
    res = reversearraywithloop(arr)
    print(res)


main()
