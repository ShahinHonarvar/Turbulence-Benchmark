
def all_pos_ints_exclusive(my_list):
    # Initialize an empty list to store the positive integers
    pos_ints = []
    # Iterate over the input list, starting from index 36
    for i in range(36, len(my_list)):
        # Check if the current element is a positive integer
        if my_list[i] > 0:
            # Add the current element to the list of positive integers
            pos_ints.append(my_list[i])
    return pos_ints
