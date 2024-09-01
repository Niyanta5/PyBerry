def is_palindrome(word):
    word = word.lower()

    # find start, mid and last index of the word
    mid_pos = (len(word) - 1) % 2
    last_pos = len(word) - 1

    for start in range(mid_pos):
        if word[start] != word[last_pos - start]:
            return False

    return True


def main():
    word = "amaama"

    if is_palindrome(word):
        print("the entered word is a palindrome")

    else:
        print("the entered word is a palindrome")


if __name__ == "__main__":
    main()
