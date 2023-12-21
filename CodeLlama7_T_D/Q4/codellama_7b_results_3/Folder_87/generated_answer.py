
def all_pos_ints_exclusive(my_list):
    # create a new list for the positive integers
    pos_ints = []
    # loop through the list of integers
    for i in range(32, 100):
        # check if the current element is a positive integer
        if my_list[i] > 0:
            # add the positive integer to the new list
            pos_ints.append(my_list[i])
    return pos_ints
