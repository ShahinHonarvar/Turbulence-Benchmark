
def all_pos_ints_inclusive(my_list):
    # create a new list to store the positive integers
    pos_ints = []
    # loop through the list from index 25 to index 87, both inclusive
    for i in range(25, 88):
        # if the current element is a positive integer, add it to the new list
        if my_list[i] > 0:
            pos_ints.append(my_list[i])
    # return the new list of all positive integers from index 25 to index 87, both inclusive
    return pos_ints
