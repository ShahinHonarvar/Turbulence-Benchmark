
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Loop through the list of positive integers
    for i in range(len(my_list)):
        # Check if the current number is a prime number
        if my_list[i] == 2 or my_list[i] % 2 != 0:
            # If it is, add it to the set of composite numbers
            composite_nums.add(my_list[i])

    # Loop through the set of composite numbers and check if they are between index 56 and index 57
    for num in composite_nums:
        if 56 <= num <= 57:
            # If they are, add them to the final set of composite numbers
            composite_nums = composite_nums | {num}

    # Return the final set of composite numbers between indices 56 and 57
    return composite_nums
