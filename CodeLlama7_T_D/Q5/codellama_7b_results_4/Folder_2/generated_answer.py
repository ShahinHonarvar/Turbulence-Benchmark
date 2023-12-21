
def all_neg_ints_inclusive(my_list):
    # Initialize an empty list to store the negative integers
    neg_ints = []
    # Loop through the list from index 15 to 39, both inclusive
    for i in range(15, 40):
        # Check if the current element is a negative integer
        if my_list[i] < 0:
            # Add the negative integer to the list of negative integers
            neg_ints.append(my_list[i])
    # Return the list of all negative integers from index 15 to index 39, both inclusive
    return neg_ints
