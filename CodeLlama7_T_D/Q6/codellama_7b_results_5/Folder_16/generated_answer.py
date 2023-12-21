
def all_neg_ints_exclusive(my_list):
    # Initialize an empty list to store the negative integers
    neg_ints = []

    # Iterate through the list from index 86 to index 90, both exclusive
    for i in range(86, 90):
        # If the current element is negative, add it to the neg_ints list
        if my_list[i] < 0:
            neg_ints.append(my_list[i])

    # Return the list of all negative integers from index 86 to index 90, both exclusive
    return neg_ints
