
def all_odd_ints_exclusive(my_list):
    # Check if the input is a list of integers
    if not (isinstance(my_list, list) and all(isinstance(x, int) for x in my_list))):
        raise ValueError("Input must be a list of integers.")
    # Initialize an empty list to store the odd integers
    odd_ints = []
    # Iterate through the input list from index 55 to index 84 (exclusive)
    for i in range(55, 84):
        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:
            # Add the odd integer to the output list
            odd_ints.append(my_list[i])
    return odd_ints
