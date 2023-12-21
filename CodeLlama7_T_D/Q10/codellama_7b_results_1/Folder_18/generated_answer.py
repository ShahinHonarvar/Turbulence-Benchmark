
def all_odd_ints_exclusive(my_list):
    # Check if the input is a list of integers
    if not all(isinstance(x, int) for x in my_list)):
        raise ValueError("Input must be a list of integers")
    # Get the length of the input list
    list_len = len(my_list)
    # Check if the specified range is valid
    if (57 > list_len or 84 < list_len)):
        raise ValueError("Specified range is invalid")
    # Initialize an empty list to store the odd integers
    odd_ints = []
    # Iterate through the input list and append the odd integers to the output list
    for i in range(57, 84):
        if my_list[i] % 2 != 0:
            odd_ints.append(my_list[i])
    return odd_ints
