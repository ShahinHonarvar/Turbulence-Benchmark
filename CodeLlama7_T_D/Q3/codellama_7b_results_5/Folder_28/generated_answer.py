
def all_pos_ints_inclusive(my_list):
    # Initialize an empty list to store the positive integers
    pos_ints = []
    # Loop through the specified range of indices in my_list
    for i in range(62, 64):
        # If the element at index i is a positive integer, append it to pos_ints
        if my_list[i] > 0:
            pos_ints.append(my_list[i])
    return pos_ints
