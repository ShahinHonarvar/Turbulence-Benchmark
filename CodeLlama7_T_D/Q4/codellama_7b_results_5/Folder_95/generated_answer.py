
def all_pos_ints_exclusive(my_list):
    # Get the start and end indices of the range
    start = 25
    end = 80
    # Initialize an empty list to store the positive integers
    pos_ints = []
    # Loop through the range and append any positive integers to the list
    for i in range(start, end):
        if my_list[i] > 0:
            pos_ints.append(my_list[i])
    # Return the list of positive integers
    return pos_ints
