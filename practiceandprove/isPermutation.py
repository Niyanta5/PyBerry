def isPermutaion(strA, strB):
    if len(strA) != len(strB):
        return False

    char_count_dict = {}

    # checking for stringA

    for char in strA:
        if char in char_count_dict:
            char_count_dict[char] += 1
        else:
            char_count_dict[char] = 1

    for char in strB:
        if char in char_count_dict and char_count_dict[char] > 0:
            char_count_dict[char] -= 1
        else:
            return False

    return True


def main():
    result = isPermutaion("abc", "dab")
    print(result)


if __name__ == "__main__":
    main()
