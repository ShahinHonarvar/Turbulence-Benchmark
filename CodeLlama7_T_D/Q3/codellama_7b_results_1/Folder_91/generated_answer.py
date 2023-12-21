
def all_pos_ints_inclusive(my_list):
    # create a new list to store the positive integers
    pos_ints = []
    # loop through the list of integers
    for i in range(len(my_list)):
        # check if the current integer is positive
        if my_list[i] > 0:
            # add the positive integer to the new list
            pos_ints.append(my_list[i])
    # return the new list of positive integers
    return pos_ints
