
def all_neg_ints_inclusive(my_list):
    # Initialize an empty list to store the negative integers
    neg_ints = []

    # Loop through the specified range of the input list
    for i in range(80, 201):
        # If the current element is a negative integer, append it to the output list
        if my_list[i] < 0:
            neg_ints.append(my_list[i])

    # Return the list of all negative integers in the specified range, or an empty list if no such integers exist
    return neg_ints
