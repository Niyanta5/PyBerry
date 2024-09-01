def canformPalindrome(strA):
    char_count_dict = {}

    for char in strA:
        if char in char_count_dict:
            char_count_dict[char] += 1
        else:
            char_count_dict[char] = 1

    odd_count = 0

    for count in char_count_dict.values():
        if count % 2 != 0:
            odd_count += 1

            if odd_count > 1:
                return False

    return True


def main():
    result = canformPalindrome("racecar")
    print(result)


if __name__ == "__main__":
    main()


