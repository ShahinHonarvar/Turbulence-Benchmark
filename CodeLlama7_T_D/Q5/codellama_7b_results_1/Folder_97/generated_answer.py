
def all_neg_ints_inclusive(my_list):
    # Initialize an empty list to store the negative integers
    neg_ints = []

    # Iterate through the specified range of indices
    for i in range(40, 81):
        # If the current index contains a negative integer, append it to the list of negative integers
        if my_list[i] < 0:
            neg_ints.append(my_list[i])

    # Return the list of all negative integers from the specified range, inclusive
    return neg_ints
