
def all_pos_ints_inclusive(my_list):
    # Initialize an empty list to store the positive integers
    pos_ints = []
    # Loop through the input list from index 29 to index 93
    for i in range(29, 94):
        # If the current element is a positive integer, add it to the list of positive integers
        if my_list[i] > 0:
            pos_ints.append(my_list[i])
    return pos_ints
