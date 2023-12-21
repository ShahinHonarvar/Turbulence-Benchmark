
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_numbers = set()

    # Iterate over the list of positive integers
    for i in range(30, 87 + 1):
        # If the number is not a prime number, it is a composite number
        if my_list[i] != 1:
            composite_numbers.add(my_list[i])

    # Return the set of all composite numbers in the specified range
    return composite_numbers
