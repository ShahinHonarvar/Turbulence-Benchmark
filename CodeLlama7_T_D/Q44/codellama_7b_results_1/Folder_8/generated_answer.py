
def composite_nums_between_indices(my_list):
    # Define a list to store the composite numbers between indices 68 and 86
    composite_nums = []

    # Iterate through the list from index 68 to index 86
    for i in range(68, 87):

        # Check if the current number is a multiple of 2 or 3
        if my_list[i] % 2 == 0 or my_list[i] % 3 == 0:

            # If it is a multiple, add it to the list of composite numbers
            composite_nums.append(my_list[i])

    # Return the set of all composite numbers between indices 68 and 86
    return set(composite_nums)
