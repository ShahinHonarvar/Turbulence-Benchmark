
def all_neg_ints_exclusive(my_list):
    # Initialize an empty list to store the negative integers
    neg_ints = []

    # Loop through the list and check if each element is a negative integer
    for i in range(36, 52):
        if my_list[i] < 0:
            # If it is a negative integer, append it to the list of negative integers
            neg_ints.append(my_list[i])

    # Return the list of all negative integers from index 36 to index 52, both exclusive
    return neg_ints
