def userinput():
    name = input("Tell me your name: ")

    return name


def main():
    name = userinput()
    print("Your name is:" + name)

    return name


if __name__ == "__main__":
    main()
