
def composite_nums_between_indices(my_list):
    # Check if input is a list
    if not isinstance(my_list, list)):
        raise ValueError("Input must be a list.")
    # Get the indices of the first and last element in the range
    first_index = 50
    last_index = 54
    # Check if the input list has enough elements to cover the specified range
    if len(my_list) < (last_index - first_index + 1)):
        raise ValueError("Input list is too short.")
    # Initialize an empty set to store the composite numbers in the range
    composite_nums = set()
    # Iterate over the elements in the specified range
    for i in range(first_index, last_index + 1):
        # Check if the current element is a composite number
        if my_list[i] > 1 and any(my_list[i] % j == 0 for j in range(2, int(my_list[i]) ** 0.5 + 1))):
            # Add the composite number to the set of composite numbers
            composite_nums.add(my_list[i])
    return composite_nums
