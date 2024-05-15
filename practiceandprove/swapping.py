def swap_list(alist):
    listsize = len(alist)

    temp = alist[0]
    alist[0] = alist[listsize - 1]
    alist[listsize - 1] = temp


def main():
    my_list = [1, 2, 3, 4, 5]
    print("Original list:", my_list)
    swap_list(my_list)
    print("List after swapping first and last elements:", my_list)


if __name__ == "__main__":
    main()
