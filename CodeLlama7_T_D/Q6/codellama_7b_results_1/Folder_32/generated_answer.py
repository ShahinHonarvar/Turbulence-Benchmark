
def all_neg_ints_exclusive(my_list):
    # initialize an empty list to store the negative integers
    neg_ints = []

    # loop through the list and check if each element is negative
    for i in range(11, 76):
        if my_list[i] < 0:
            # if the element is negative, append it to the list of negative integers
            neg_ints.append(my_list[i])

    # return the list of all negative integers from index 11 to index 76, both exclusive
    return neg_ints
