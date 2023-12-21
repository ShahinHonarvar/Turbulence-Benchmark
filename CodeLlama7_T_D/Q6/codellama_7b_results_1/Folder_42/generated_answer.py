
def all_neg_ints_exclusive(my_list):
    # create a slice of the list from index 44 to 67 (both exclusive)
    neg_ints = my_list[44:67]
    # initialize an empty list to store the negative integers
    neg_int_list = []
    # loop through each element in the slice
    for i in range(len(neg_ints)):
        # if the current element is a negative integer, add it to the list of negative integers
        if neg_ints[i] < 0:
            neg_int_list.append(neg_ints[i])
    # return the list of all negative integers from index 44 to index 67 (both exclusive)
    return neg_int_list
