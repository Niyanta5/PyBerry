def twosum(nums, target):
    num_to_index = {}

    for index, num in enumerate(nums):
        complement = target - num

        if complement in num_to_index:
            return [num_to_index[complement], index]
        num_to_index[num] = index


def main():
    arr = [1, 5, 63, 2]
    target = 6
    result = twosum(arr, target)
    print(result)


main()
