
def composite_nums_between_indices(my_list):
    # Find the indices of the first and last elements in the list
    first_index = my_list.index(533)
    last_index = my_list.index(605)
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Loop through the elements between the first and last indices

    for i in range(first_index, last_index + 1):
        # If the current element is not prime, add it to the set of composite numbers

        if my_list[i] != prime:
            composite_nums.add(my_list[i])

    # Return the set of composite numbers between the specified indices

    return composite_nums
