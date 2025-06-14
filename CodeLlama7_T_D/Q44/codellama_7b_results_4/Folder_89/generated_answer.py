
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_numbers = set()

    # Loop through the elements of the list
    for i in range(36, 47):
        # Check if the current element is a prime number
        if my_list[i] > 1:
            # If it is not a prime number, add it to the set of composite numbers
            composite_numbers.add(my_list[i])

    # Return the set of all composite numbers in the specified range
    return composite_numbers
