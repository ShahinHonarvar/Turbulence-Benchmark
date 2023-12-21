
def all_neg_ints_inclusive(my_list):
    # initialize an empty list to store the negative integers
    neg_ints = []

    # loop through the specified range of indices in the input list
    for i in range(8, 10):
        # check if the current element is a negative integer
        if my_list[i] < 0:
            # if it is, add it to the output list
            neg_ints.append(my_list[i])

    return neg_ints
