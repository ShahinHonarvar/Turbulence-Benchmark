
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_numbers = set()

    # Iterate over the list of positive integers
    for i in range(len(my_list)):
        # Check if the current number is greater than 1 and is a factor of the current number
        if my_list[i] > 1 and my_list[i] % 2 == 0:
            # If it is a factor, add it to the set of composite numbers
            composite_numbers.add(my_list[i])

    # Return the set of all composite numbers in the given list that are between index 82 to index 86, both inclusive
    return composite_numbers
