
def all_pos_ints_exclusive(my_list):
    # Define a range of positive integers starting from index 44 and ending at index 91 (both exclusive)
    pos_int_range = range(44, 91)
    # Initialize an empty list to store the positive integers in the specified range
    pos_ints = []
    # Iterate over the range of positive integers
    for i in pos_int_range:
        # Check if the current index corresponds to a positive integer in the input list
        if my_list[i] > 0:
            # If it does, add it to the list of positive integers
            pos_ints.append(my_list[i])
    # Return the list of positive integers in the specified range (empty if none exist)
    return pos_ints
