
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate over the list of positive integers
    for i in range(40, 81):
        # Check if the current number is prime or not
        if my_list[i] > 1:
            # If it is prime, add it to the set of composite numbers
            composite_nums.add(my_list[i])

    # Return the set of all composite numbers in the given list that are between index 40 to index 80, both inclusive.
    return composite_nums
