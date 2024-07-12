def twoSum(nums, target):
    complement_dict = {}

    # Iterate through the list with both index and number

    for index, num in enumerate(nums):
        # Calculate the complement that would sum with the current number to reach the target

        complement = target - num

        # Check if the complement exists in the dictionary

        if complement in complement_dict:
            # If found, return the index of the complement and the current index

            return [complement_dict[complement], index]

        # Otherwise, add the current number and its index to the dictionary
        complement_dict[num] = index

    return []


def main():
    # Test the twoSum function with a sample input
    result = twoSum([2, 4, 6, 4, 55, 89], 59)
    print(result)  # Output: [3, 4] as 4 (index 3) + 55 (index 4) = 59


if __name__ == "__main__":
    main()
