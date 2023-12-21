
def composite_nums_between_indices(my_list):
    # Create an empty set to store the composite numbers
    composite_numbers = set()

    # Iterate over the list of positive integers
    for i in range(len(my_list)):
        # If the current number is divisible by 2, 3, or 5, it is a prime number and should be added to the set of composite numbers
        if my_list[i] % 2 == 0 or my_list[i] % 3 == 0 or my_list[i] % 5 == 0:
            composite_numbers.add(my_list[i])

    # Return the set of all composite numbers in the given list that are between index 69 to index 83, both inclusive
    return composite_numbers
