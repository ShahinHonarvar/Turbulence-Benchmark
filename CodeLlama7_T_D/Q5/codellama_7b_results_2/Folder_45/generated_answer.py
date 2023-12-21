
def all_neg_ints_inclusive(my_list):
    # Initialize an empty list to store the negative integers
    neg_ints = []
    # Loop through the specified range of the input list
    for i in range(30, 201):
        # Check if the current element is a negative integer
        if my_list[i] < 0:
            # If it is, add it to the output list
            neg_ints.append(my_list[i])
    # Return the output list of negative integers
    return neg_ints
