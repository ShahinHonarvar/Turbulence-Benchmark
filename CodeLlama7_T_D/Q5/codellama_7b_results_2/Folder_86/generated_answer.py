
def all_neg_ints_inclusive(my_list):
    # Initialize an empty list to store the negative integers
    neg_ints = []

    # Loop through the specified range of indices in my_list
    for i in range(31, 35):

        # If the current index is a negative integer, add it to the neg_ints list
        if my_list[i] < 0:
            neg_ints.append(my_list[i])

    # Return the neg_ints list
    return neg_ints
