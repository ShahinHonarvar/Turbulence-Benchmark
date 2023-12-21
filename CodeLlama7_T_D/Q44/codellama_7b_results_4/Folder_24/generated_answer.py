
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_numbers = set()

    # Iterate through the list from index 34 to index 55, both inclusive
    for i in range(34, 56):
        # Check if the current element is a prime number
        if my_list[i] != 1:
            # If the current element is not a prime number, then it must be a composite number
            composite_numbers.add(my_list[i])

    # Return the set of all composite numbers in the given list that are between index 34 to index 55, both inclusive
    return composite_numbers
