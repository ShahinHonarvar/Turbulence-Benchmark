
def composite_nums_between_indices(my_list):
    # Check if the input is a list
    if not isinstance(my_list, list)):
        raise ValueError("Input must be a list")
    # Define the range of indices to consider
    start_index = 90
    end_index = 200
    # Initialize an empty set to store the composite numbers
    composite_nums = set()
    # Loop over the elements in the given list within the specified range
    for i in range(start_index, end_index + 1):
        # Check if the current element is a prime number
        if my_list[i] % 2 == 0 and my_list[i] != 2:
            # Add the composite number to the set of composite numbers
            composite_nums.add(my_list[i])
    return composite_nums
