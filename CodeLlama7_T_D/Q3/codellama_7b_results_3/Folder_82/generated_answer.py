
def all_pos_ints_inclusive(my_list):
    # Check if the input is a list of integers
    if not all(isinstance(x, int) for x in my_list)):
        raise ValueError("Input must be a list of integers")
    # Initialize an empty list to store the positive integers
    pos_ints = []
    # Iterate through the input list and append each positive integer to the output list
    for i in range(len(my_list)):
        if my_list[i] > 0:
            pos_ints.append(my_list[i])
    # Return the list of all positive integers from index 20 to index 200, both inclusive
    return pos_ints
