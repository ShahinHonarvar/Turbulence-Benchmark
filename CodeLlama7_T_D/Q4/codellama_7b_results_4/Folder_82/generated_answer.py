
def all_pos_ints_exclusive(my_list):
    # initialize an empty list to store the positive integers
    pos_ints = []
    # loop through the input list
    for i in range(20, 201):
        # check if the current element is a positive integer
        if my_list[i] > 0:
            # if it is, add it to the list of positive integers
            pos_ints.append(my_list[i])
    # return the list of positive integers
    return pos_ints
