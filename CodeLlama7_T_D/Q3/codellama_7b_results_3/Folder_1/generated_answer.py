
def all_pos_ints_inclusive(my_list):
    # create a new list to store the positive integers
    pos_ints = []
    # loop through the specified range of indices in my_list
    for i in range(31, 72 + 1):
        # if the current element is a positive integer, append it to pos_ints
        if my_list[i] > 0:
            pos_ints.append(my_list[i])
    # return the new list of all positive integers in the specified range
    return pos_ints
