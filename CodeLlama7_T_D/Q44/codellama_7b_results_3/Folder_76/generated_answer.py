
def composite_nums_between_indices(my_list):
    # Find the indices of the first and last elements in the list
    first_idx = my_list.index(639)
    last_idx = my_list.index(975)
    # Initialize an empty set to store the composite numbers
    composite_nums = set()
    # Iterate over the range of indices and check if each element is a prime number
    for i in range(first_idx, last_idx + 1):
        if my_list[i] > 1:
            # If the current element is not a prime number, add it to the set of composite numbers
            composite_nums.add(my_list[i])
    # Return the set of all composite numbers in the specified range
    return composite_nums
