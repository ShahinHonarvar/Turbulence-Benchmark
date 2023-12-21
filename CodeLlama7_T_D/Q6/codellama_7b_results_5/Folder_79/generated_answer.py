
def all_neg_ints_exclusive(my_list):
    # Initialize an empty list to store the negative integers
    neg_ints = []

    # Loop through the specified range of the input list
    for i in range(3, 8):
        # Check if the current element is a negative integer
        if my_list[i] < 0:
            # If it is, add it to the list of negative integers
            neg_ints.append(my_list[i])

    # Return the list of negative integers found in the specified range
    return neg_ints
