def reverseString(s):
    reversed_string = ""

    for char in s:
        reversed_string = char + reversed_string

    return reversed_string


def main():
    original_string = "hello"
    reversed_string = reverseString(original_string)
    print(f"Original string: {original_string}")
    print(f"Reversed string: {reversed_string}")


if __name__ == "__main__":
    main()
