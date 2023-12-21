 def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_numbers = set()

    # Iterate over the list of positive integers
    for i in range(29, 51 + 1):
        # Check if the current number is prime
        if my_list[i] == 1:
            # If it's not prime, add it to the set of composite numbers
            composite_numbers.add(my_list[i])

    # Return the set of all composite numbers in the given list that are between index 29 to index 51, both inclusive
    return composite_numbers
