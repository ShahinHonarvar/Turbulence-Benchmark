
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate through the list from index 74 to index 95, both inclusive
    for i in range(74, 96):

        # Check if the number at the current index is prime
        if my_list[i] == 1:

            # If the number is prime, add it to the set of composite numbers
            composite_nums.add(my_list[i])

    # Return the set of all composite numbers in the specified range
    return composite_nums
