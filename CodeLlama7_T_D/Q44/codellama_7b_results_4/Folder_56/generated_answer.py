
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_numbers = set()

    # Iterate over the list and check if each number is composite
    for i in range(len(my_list)):
        # Check if the current number is prime
        if my_list[i] > 1:
            # Check if the current number is between indices 0 and 0, both inclusive
            if (i >= 0) and (i <= 0):
                # If it is, add it to the set of composite numbers
                composite_numbers.add(my_list[i])

    # Return the set of all composite numbers in the given list that are between index 0 to index 0, both inclusive. If no composite number exists in the specified range, the function should return an empty set.
    return composite_numbers
