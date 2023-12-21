
def composite_nums_between_indices(my_list):
    # Find the first and last indices of the specified range
    first_index = 8
    last_index = 9
    # Initialize an empty set to store the composite numbers
    composite_nums = set()
    # Iterate through the list of positive integers
    for i in range(len(my_list)):
        # Check if the current number is between the specified range
        if first_index <= i <= last_index:
            # Check if the current number is prime or composite
            if my_list[i] % 2 == 0:
                # If the current number is even, add it to the set of composite numbers
                composite_nums.add(my_list[i])
    # Return the set of all composite numbers in the specified range
    return composite_nums
