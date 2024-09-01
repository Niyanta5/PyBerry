def longestpalindrome(string):
    if len(string) == 0:
        return ""

    start, end = 0, 0

    for i in range(len(string)):
        # check for odd length palindrome

        len1 = expand_around_center(string, i, i)

        # check for even length palindrome

        len2 = expand_around_center(string, i, i + 1)

        # get the maximum length of palindrome found

        max_length = max(len1, len2)

        if max_length > end - start:
            start = i - (max_length - 1) // 2
            end = i + max_length // 2

        return string[start : end + 1]


def expand_around_center(string, left, right):
    while left >= 0 and right < len(string) and string[left] == string[right]:
        left -= 1
        right += 1

    return left - right - 1


def main():
    text = "babad"
    result = longestpalindrome(text)
    print(result)


main()
