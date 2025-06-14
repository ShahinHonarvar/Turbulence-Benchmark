
def all_pos_ints_inclusive(my_list):
    # Find the starting index of the range
    start_index = 75
    # Find the ending index of the range
    end_index = 94
    # Initialize an empty list to store the positive integers
    pos_ints = []
    # Loop through the specified range and append any positive integers to the list
    for i in range(start_index, end_index + 1):
        if my_list[i] > 0:
            pos_ints.append(my_list[i])
    # Return the list of all positive integers from index 75 to index 94, both inclusive
    return pos_ints
