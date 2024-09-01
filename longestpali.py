def longest_palindromic_substring(s):
    if len(s) == 0:
        return ""

    start, end = 0, 0

    for i in range(len(s)):
        # Check for odd-length palindromes
        len1 = expand_around_center(s, i, i)
        # Check for even-length palindromes
        len2 = expand_around_center(s, i, i + 1)
        # Get the maximum length of palindrome found
        max_len = max(len1, len2)

        if max_len > end - start:
            start = i - (max_len - 1) // 2
            end = i + max_len // 2

    return s[start : end + 1]


def expand_around_center(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1

    return right - left - 1


# Example usage
s = "babad"
print(longest_palindromic_substring(s))  # Output: "bab" or "aba"
