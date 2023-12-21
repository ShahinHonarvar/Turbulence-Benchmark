
def all_neg_ints_exclusive(my_list):
    # Initialize an empty list to store the negative integers
    neg_ints = []

    # Iterate through the list from index 66 to index 90, exclusive
    for i in range(66, 91):
        # If the current element is a negative integer, add it to the list of negative integers
        if my_list[i] < 0:
            neg_ints.append(my_list[i])

    # Return the list of all negative integers from index 66 to index 90, exclusive
    return neg_ints
