
def all_pos_ints_inclusive(my_list):
    # create a new list to store the positive integers
    pos_ints = []
    # loop through the specified range of indices in my_list
    for i in range(20, 201):
        # if the element at index i is a positive integer, append it to pos_ints
        if my_list[i] > 0:
            pos_ints.append(my_list[i])
    # return pos_ints, which contains all the positive integers from index 20 to index 200, both inclusive
    return pos_ints
