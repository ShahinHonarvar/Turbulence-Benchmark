 def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_numbers = set()

    # Iterate over the list and check if each number is composite between indices 17 and 78
    for i in range(len(my_list)):
        # Check if the current number is composite
        if is_composite(my_list[i]):
            # If it is, check if it falls within the specified range
            if 17 <= i <= 78:
                # If it does, add it to the set of composite numbers
                composite_numbers.add(my_list[i])

    # Return the set of all composite numbers in the given list that are between index 17 and 78, both inclusive
    return composite_numbers
