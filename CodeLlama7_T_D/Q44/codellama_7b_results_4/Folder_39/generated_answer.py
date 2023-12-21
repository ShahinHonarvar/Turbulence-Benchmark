
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate over the list of positive integers
    for i in range(len(my_list)):
        # Check if the current number is a prime number
        if my_list[i] == 1 or my_list[i] % 2 == 0:
            # If the current number is not a prime number, it must be a composite number
            composite_nums.add(my_list[i])

    # Return the set of all composite numbers in the specified range
    return composite_nums
