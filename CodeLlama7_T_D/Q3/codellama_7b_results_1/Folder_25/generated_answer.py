
def all_pos_ints_inclusive(my_list):
    # Initialize an empty list to store the positive integers
    pos_ints = []
    # Loop through the specified range of indices in my_list
    for i in range(29, 94):
        # If the element at index i in my_list is positive, add it to the pos_ints list
        if my_list[i] > 0:
            pos_ints.append(my_list[i])
    # Return the pos_ints list
    return pos_ints
