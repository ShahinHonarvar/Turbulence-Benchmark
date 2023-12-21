
def all_neg_ints_exclusive(my_list):
    # Initialize an empty list to store the negative integers
    neg_ints = []

    # Loop through the specified range of indices in the input list
    for i in range(56, 89):
        # Check if the current element is a negative integer
        if my_list[i] < 0:
            # Add the current element to the list of negative integers
            neg_ints.append(my_list[i])

    return neg_ints
