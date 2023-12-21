
def all_pos_ints_inclusive(my_list):
    # Initialize an empty list to store the positive integers
    pos_ints = []
    # Loop through the specified range of indices in the input list
    for i in range(50, 55):
        # Check if the element at the current index is a positive integer
        if my_list[i] > 0:
            # If it is, add it to the list of positive integers
            pos_ints.append(my_list[i])
    return pos_ints
