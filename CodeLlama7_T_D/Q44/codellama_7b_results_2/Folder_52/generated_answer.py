
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate through the list of positive integers
    for i in range(62, 100):
        # If the current number is a prime number, add it to the set
        if my_list[i] == 1:
            composite_nums.add(my_list[i])

    # Return the set of all composite numbers in the specified range
    return composite_nums
