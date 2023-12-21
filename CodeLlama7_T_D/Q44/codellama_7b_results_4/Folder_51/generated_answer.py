
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate over the list of positive integers
    for i in range(len(my_list)):
        # Check if the current number is greater than 1 and is a factor of its own index plus 8
        if my_list[i] > 1 and my_list[i] % (i + 8) == 0:
            # If it is, add it to the set of composite numbers
            composite_nums.add(my_list[i])

    # Return the set of all composite numbers in the given list that are between index 1 and index 8, both inclusive
    return composite_nums
