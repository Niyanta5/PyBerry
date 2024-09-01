def swapposition(alist, pos1, pos2):
    if pos1 >= 0 and pos2 >= 0 and pos1 < len(alist) and pos2 < len(alist):
        alist[pos1], alist[pos2] = alist[pos2], alist[pos1]

    return alist


def main():
    alist = [32, 134, 52, 754]
    pos1, pos2 = 1, 3

    result = swapposition(alist, pos1, pos2)
    print(result)


if __name__ == "__main__":
    main()
