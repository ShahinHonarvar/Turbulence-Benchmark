
def all_neg_ints_inclusive(my_list):
    # Initialize an empty list to store the negative integers
    neg_ints = []
    # Loop through the list from index 62 to 92, both inclusive
    for i in range(62, 93):
        # Check if the current element is a negative integer
        if my_list[i] < 0:
            # If it is, add it to the list of negative integers
            neg_ints.append(my_list[i])
    # Return the list of all negative integers in the specified range
    return neg_ints
