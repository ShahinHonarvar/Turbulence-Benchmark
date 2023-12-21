
def all_pos_ints_exclusive(my_list):
    # Check if the input list is a list of integers
    if not all(isinstance(x, int) for x in my_list)):
        raise ValueError("Input must be a list of integers")
    # Initialize an empty list to store the positive integers
    pos_ints = []
    # Iterate through the input list and append the positive integers to the output list
    for i in range(10, 76):
        if my_list[i] > 0:
            pos_ints.append(my_list[i])
    # Return the list of all positive integers from index 10 to index 76, both exclusive
    return pos_ints
