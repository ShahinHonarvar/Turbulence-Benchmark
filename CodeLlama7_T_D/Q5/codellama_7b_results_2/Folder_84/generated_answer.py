
def all_neg_ints_inclusive(my_list):
    # Initialize an empty list to store the negative integers
    neg_ints = []
    # Loop through the indices of the input list
    for i in range(43, 87):
        # Check if the current index contains a negative integer
        if my_list[i] < 0:
            # If it does, add it to the list of negative integers
            neg_ints.append(my_list[i])
    return neg_ints
