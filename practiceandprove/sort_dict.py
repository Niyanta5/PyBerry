def sort_dict(input_dict):
    keys = list(input_dict.keys())

    for i in range(len(keys)):
        for j in range(0, n - i - 1):
            if keys[j] > keys[j + 1]:
                keys[j], keys[j + 1] = keys[j + 1], keys[j]

    sorted_dict = {key: input_dict[key] for key in keys}

    return sorted_dict


def main():
    myDict = {"n": 4, "p": 3}
    sorted_dict = sort_dict(myDict)
    print(sorted_dict)


# Call the main function

if __name__ == "__main__":
    main()
