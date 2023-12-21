
def composite_nums_between_indices(my_list):
    # Check if the input is a list of positive integers
    if not all(isinstance(x, int) and x > 0 for x in my_list)):
        raise ValueError("Input must be a list of positive integers")
    # Define the range of indices to check
    start_index = 56
    end_index = 98
    # Initialize an empty set to store the composite numbers
    composite_numbers = set()

    # Iterate over the elements in the specified range
    for i in range(start_index, end_index + 1):
        # Check if the element is a prime number
        if my_list[i] > 1:
            # If it is a prime number, add it to the set of composite numbers
            composite_numbers.add(my_list[i])

    # Return the set of all composite numbers in the given list that are between index 56 to index 98, both inclusive
    return composite_numbers
