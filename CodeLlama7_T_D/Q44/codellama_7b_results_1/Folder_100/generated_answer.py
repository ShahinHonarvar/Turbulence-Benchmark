 def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()
    # Iterate over the list from index 12 to index 92, both inclusive
    for i in range(12, 93):
        # Check if the current element is a prime number
        if my_list[i] == 1:
            # If it is a prime number, add it to the set of composite numbers
            composite_nums.add(my_list[i])
    # Return the set of all composite numbers in the specified range
    return composite_nums
