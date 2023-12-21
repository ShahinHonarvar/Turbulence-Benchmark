
def all_neg_ints_exclusive(my_list):
    # Initialize an empty list to store the negative integers
    neg_ints = []
    # Loop through the list of integers
    for i in range(11, 76):
        # Check if the current element is negative
        if my_list[i] < 0:
            # Add the negative integer to the list
            neg_ints.append(my_list[i])
    return neg_ints
