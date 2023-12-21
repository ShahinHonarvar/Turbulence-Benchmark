
def all_neg_ints_inclusive(my_list):
    # Initialize an empty list to store the negative integers
    neg_ints = []
    # Loop through the specified range of indices in the input list
    for i in range(56, 58):
        # Check if the current element is a negative integer
        if my_list[i] < 0:
            # If it is, add it to the output list
            neg_ints.append(my_list[i])
    # Return the list of all negative integers in the specified range
    return neg_ints
