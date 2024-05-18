def sort_dict_by_values(input_dict):
    values = list(input_dict.values())
    keys = list(input_dict.keys())

    for i in range(len(values)):
        for j in range(len(values) - i - 1):
            if values[j] > values[j + 1]:
                values[j], values[j + 1] = values[j + 1], values[j]
                # now update the keys as well
                keys[j], keys[j + 1] = keys[j + 1], keys[j]
    sorted_dict = {keys[i]: values[i] for i in range(len(keys))}

    return sorted_dict


def main():
    my_dict = {"n": 4, "p": 3, "a": 2}
    sorted_dict = sort_dict_by_values(my_dict)
    print("Original: ", my_dict)
    print("sorted_dict: ", sorted_dict)


if __name__ == "__main__":
    main()
