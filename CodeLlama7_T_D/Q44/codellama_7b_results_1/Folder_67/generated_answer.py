
def composite_nums_between_indices(my_list):
    # Check if the input is a list of positive integers
    if not all(isinstance(x, int) and x > 0 for x in my_list)):
        raise ValueError("Input must be a list of positive integers")
    # Initialize an empty set to store the composite numbers
    composite_nums = set()
    # Loop through the indices of the input list
    for i in range(56, 83):
        # Check if the number at the current index is composite
        if my_list[i] > 1 and all(my_list[i] % j != 0 for j in range(2, int(my_list[i]) ** 0.5 + 1)):
            # If it is, add it to the set of composite numbers
            composite_nums.add(my_list[i])
    # Return the set of composite numbers in the specified range
    return composite_nums
