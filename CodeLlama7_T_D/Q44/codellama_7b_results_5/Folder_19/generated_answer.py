
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_numbers = set()

    # Iterate over the list of positive integers
    for i in range(len(my_list)):
        # Check if the current number is composite
        if my_list[i] > 1 and my_list[i] % 2 != 0:
            # If it is, add it to the set of composite numbers
            composite_numbers.add(my_list[i])

    # Return the set of all composite numbers between index 5 and index 7, both inclusive
    return composite_numbers
