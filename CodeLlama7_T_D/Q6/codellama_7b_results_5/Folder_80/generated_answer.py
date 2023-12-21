
def all_neg_ints_exclusive(my_list):
    # Initialize an empty list to store the negative integers
    neg_ints = []

    # Loop through the specified range of indices in my_list
    for i in range(69, 97):

        # If the current element is negative, add it to the neg_ints list
        if my_list[i] < 0:
            neg_ints.append(my_list[i])

    # Return the list of all negative integers from index 69 to index 97, both exclusive
    return neg_ints
