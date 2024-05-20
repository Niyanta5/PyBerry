def count_occurence_in_list(lst, x):
    count = 0

    for ele in lst:
        if ele == x:
            count += 1

    return count


def main():
    lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
    x = 8
    result = count_occurence_in_list(lst, x)
    print(f"{x} has occurred {result} times")


if __name__ == "__main__":
    main()
