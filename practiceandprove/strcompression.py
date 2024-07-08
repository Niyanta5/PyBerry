def strCompression(string):
    if string == "":
        return ""

    current = string[0]
    result = ""
    count = 1

    for i in range(1, len(string)):
        if string[i] == current:
            count += 1
        else:
            result += current + str(count)
            current = string[i]
            count = 1
    result += current + str(count)

    return "".join(result)


def main():
    result = strCompression("aaabbc")
    print(result)


if __name__ == "__main__":
    main()
