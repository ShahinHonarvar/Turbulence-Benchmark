
def all_neg_ints_inclusive(my_list):
    # initialize an empty list to store the negative integers
    neg_ints = []

    # loop through the specified range of indices in the input list
    for i in range(31, 35):

        # check if the current element is a negative integer
        if my_list[i] < 0:

            # if it is, add it to the list of negative integers
            neg_ints.append(my_list[i])

    # return the list of all negative integers from index 31 to index 34, both inclusive
    return neg_ints
