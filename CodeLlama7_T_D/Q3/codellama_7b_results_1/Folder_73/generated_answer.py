
def all_pos_ints_inclusive(my_list):
    # Initialize an empty list to store the positive integers
    pos_ints = []
    # Iterate through the specified range of indices in my_list
    for i in range(19, 93):
        # Check if the current element is a positive integer
        if isinstance(my_list[i], int) and my_list[i] > 0:
            # If it is, add it to the list of positive integers
            pos_ints.append(my_list[i])
    return pos_ints
