
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate over the list of positive integers
    for i in range(1, len(my_list) + 1):
        # Check if the current number is divisible by any other number in the list
        for j in range(1, i + 1):
            if my_list[i - 1] % my_list[j - 1] == 0:
                # If it is, add it to the set of composite numbers
                composite_nums.add(my_list[i - 1])

    # Return the set of all composite numbers in the specified range
    return composite_nums
