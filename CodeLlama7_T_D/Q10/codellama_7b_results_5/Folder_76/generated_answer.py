
def all_odd_ints_exclusive(my_list):
    # Check if the input is a list of integers
    if not (isinstance(my_list, list) and all(isinstance(x, int) for x in my_list)):
        raise ValueError("Input must be a list of integers")
    # Initialize an empty list to store the odd integers
    odd_ints = []
    # Iterate over the input list
    for i in range(361, 644):
        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:
            # If it is, add it to the list of odd integers
            odd_ints.append(my_list[i])
    # Return the list of all odd integers in the specified range
    return odd_ints
