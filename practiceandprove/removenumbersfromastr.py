def remove_numbers_from_a_str(s):
    # creating an empty str to strore the characters other than digits
    new_str = ""
    digits = "0123456789"

    for char in s:
        if char not in digits:
            # if its not a digit, append it to the new string
            new_str += char

    return new_str


def main():
    new_str = input("Enter a string: ")
    result = remove_numbers_from_a_str(new_str)
    print("String after removing numbers: ", result)


if __name__ == "__main__":
    main()
