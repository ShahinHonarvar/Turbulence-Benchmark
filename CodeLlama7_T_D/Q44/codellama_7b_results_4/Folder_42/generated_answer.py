
def composite_nums_between_indices(my_list):
    # Check if the input is a list of positive integers
    if not all(isinstance(x, int) and x > 0 for x in my_list)):
        raise ValueError("Input must be a list of positive integers")
    # Initialize an empty set to store the composite numbers
    composite_nums = set()
    # Iterate over the input list
    for i in range(len(my_list))):
        # Check if the current number is prime or not
        if my_list[i] == 1 or my_list[i] % my_list[i - 1]) == 0:
            # If the current number is prime, continue to the next iteration
            continue

        # If the current number is composite, add it to the set of composite numbers
        composite_nums.add(my_list[i])
    # Return the set of all composite numbers in the specified range
    return composite_nums
