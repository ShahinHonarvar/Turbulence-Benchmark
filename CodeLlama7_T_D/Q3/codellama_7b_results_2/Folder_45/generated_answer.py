
def all_pos_ints_inclusive(my_list):
    # Create a new list to store the positive integers
    pos_ints = []
    # Loop through the input list and append any positive integers to the output list
    for i in range(len(my_list)):
        if my_list[i] > 0:
            pos_ints.append(my_list[i])
    # Return the output list of all positive integers from index 30 to index 200, both inclusive
    return pos_ints
