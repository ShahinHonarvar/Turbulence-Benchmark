
def all_neg_ints_exclusive(my_list):
    # Initialize an empty list to store the negative integers
    neg_ints = []
    # Iterate through the specified range of the input list
    for i in range(29, 53):
        # Check if the current element is a negative integer
        if my_list[i] < 0:
            # Add the current element to the list of negative integers
            neg_ints.append(my_list[i])
    # Return the list of all negative integers from index 29 to index 53, both exclusive
    return neg_ints
