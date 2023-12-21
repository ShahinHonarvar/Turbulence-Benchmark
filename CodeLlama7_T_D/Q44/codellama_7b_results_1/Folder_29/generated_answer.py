
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate through the list of positive integers
    for i in range(52, 71 + 1):
        # Check if the current number is composite
        if my_list[i] > 1 and all(my_list[i] % j != 0 for j in range(2, int(my_list[i]) ** 0.5 + 1)):
            # If it is composite, add it to the set of composite numbers
            composite_nums.add(my_list[i])

    # Return the set of all composite numbers in the specified range
    return composite_nums
