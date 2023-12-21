
def all_neg_ints_exclusive(my_list):
    # Create an empty list to store the negative integers
    neg_ints = []

    # Loop through the specified range of the input list
    for i in range(len(my_list)):
        # Check if the current element is a negative integer
        if my_list[i] < 0:
            # If it is, add it to the output list
            neg_ints.append(my_list[i])

    # Return the list of all negative integers from index 0 to index 9, both exclusive
    return neg_ints
