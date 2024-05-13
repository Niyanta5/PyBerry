def condition2(num):
    num = int(num)

    if num > 850:
        print("Give the final test")

    elif num > 700 and num <= 850:
        print("Start giving mock tests")

    else:
        print("Extensive Revision Needed")


def main():
    num = input("Enter the num: ")
    condition2(num)


if __name__ == "__main__":
    main()
