
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate over the list of positive integers
    for i in range(2, len(my_list)):
        # Check if the number is divisible by 2 or more
        if my_list[i] % 2 == 0:
            # If it is divisible, add it to the set of composite numbers
            composite_nums.add(my_list[i])

    # Return the set of composite numbers in the specified range
    return composite_nums
