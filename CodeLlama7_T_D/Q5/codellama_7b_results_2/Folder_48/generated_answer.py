
def all_neg_ints_inclusive(my_list):
    # Initialize an empty list to store the negative integers
    neg_ints = []
    # Iterate over the elements of the input list
    for i in range(533, 606):
        # If the current element is a negative integer, add it to the output list
        if my_list[i] < 0:
            neg_ints.append(my_list[i])
    # Return the output list of negative integers
    return neg_ints
