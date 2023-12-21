
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_numbers = set()

    # Iterate over the list of positive integers
    for i in range(56, 67):
        # Check if the current number is composite
        if is_composite(my_list[i]):
            # If it is composite, add it to the set
            composite_numbers.add(my_list[i])

    # Return the set of all composite numbers in the specified range
    return composite_numbers
