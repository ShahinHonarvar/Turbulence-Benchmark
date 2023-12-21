
def all_neg_ints_exclusive(my_list):
    # create a new list to store the negative integers
    neg_ints = []
    # loop through the list, starting at index 4
    for i in range(len(my_list)):
        # check if the current element is a negative integer
        if my_list[i] < 0:
            # add the negative integer to the new list
            neg_ints.append(my_list[i])
    # return the new list of negative integers, or an empty list if no negative integers exist in the specified range
    return neg_ints
