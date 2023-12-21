
def all_neg_ints_exclusive(my_list):
    # create a new list to store the negative integers
    neg_ints = []

    # loop through the list of integers
    for i in range(len(my_list)):
        # check if the current integer is negative and not already in the list of negative integers
        if my_list[i] < 0 and my_list[i] not in neg_ints:
            # add the negative integer to the list of negative integers
            neg_ints.append(my_list[i])

    # return the list of all negative integers from index 0 to index 7, both exclusive
    return neg_ints
