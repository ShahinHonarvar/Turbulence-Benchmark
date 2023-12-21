
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_numbers = set()

    # Loop through the list from index 64 to index 66, both inclusive
    for i in range(64, 67):
        # Check if the number at the current index is prime
        if my_list[i] % 2 == 0 or my_list[i] % 3 == 0:
            # If it's not prime, add it to the set of composite numbers
            composite_numbers.add(my_list[i])

    # Return the set of composite numbers found in the specified range
    return composite_numbers
