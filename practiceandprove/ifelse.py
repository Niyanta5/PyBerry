def condition(age):
    age = int(age)

    if age > 8:
        print("can watch Netflix Kids")
    elif age < 16 and age > 8:
        print("can play Pubg and watch Netflix Kids")
    else:
        print("can watch Netflix")


def main():
    age = input("Enter your age: ")
    condition(age)


if __name__ == "__main__":
    main()
