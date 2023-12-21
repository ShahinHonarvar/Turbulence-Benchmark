
def all_neg_ints_inclusive(my_list):
    # Initialize an empty list to store the negative integers
    neg_ints = []

    # Loop through the list from index 13 to index 68 (both inclusive)
    for i in range(13, 69):
        # If the current element is a negative integer, append it to the list of negative integers
        if my_list[i] < 0:
            neg_ints.append(my_list[i])

    # Return the list of all negative integers from index 13 to index 68 (both inclusive), or an empty list if no negative integers exist in the specified range
    return neg_ints
