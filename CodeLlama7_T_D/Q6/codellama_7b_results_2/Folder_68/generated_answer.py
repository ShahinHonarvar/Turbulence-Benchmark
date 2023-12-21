
def all_neg_ints_exclusive(my_list):
    # create an empty list to store the negative integers
    neg_ints = []

    # loop through the list of integers
    for i in range(len(my_list)):
        # check if the current element is a negative integer
        if my_list[i] < 0:
            # add the negative integer to the list of negative integers
            neg_ints.append(my_list[i])

    # return the list of negative integers
    return neg_ints
