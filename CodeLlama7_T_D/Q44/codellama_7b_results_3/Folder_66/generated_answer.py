
def composite_nums_between_indices(my_list):
    # Check if the input is a list of positive integers
    if not all(isinstance(x, int) and x > 0 for x in my_list)):
        raise ValueError("Input must be a list of positive integers")
    # Initialize an empty set to store the composite numbers
    composite_nums = set()
    # Iterate through the input list
    for i in range(len(my_list))):
        # Check if the current number is divisible by any other number in the list
        for j in range(i + 1, len(my_list))):
            if my_list[i] % my_list[j] == 0:
                # If it is, add it to the set of composite numbers
                composite_nums.add(my_list[i])
    # Return the set of composite numbers in the specified range
    return composite_nums
