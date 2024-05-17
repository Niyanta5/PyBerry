def remove_char_at_index(s, index):
    if index < 0 or index >= len(s):
        raise ValueError("Index out of range")

    # using generator to skip the character specified at index

    new_str = "".join(char for i, char in enumerate(s) if i != index)

    return new_str


def main():
    new_str = input("Enter a str: ")
    index = int(input("Endex the index of the character to remove: "))
    try:
        result = remove_char_at_index(new_str, index)
        print("String after removing character: ", result)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
