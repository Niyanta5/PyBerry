def isduplicate(str):
    adict = {}

    for char in str:
        if char in adict:
            return True
        else:
            adict[char] = 1

    return False


def main():
    result = isduplicate("abcd")
    print(result)


if __name__ == "__main__":
    main()

