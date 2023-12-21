
def all_neg_ints_inclusive(my_list):
    # Initialize an empty list to store the negative integers
    neg_ints = []
    # Iterate through the list from index 43 to index 51, both inclusive
    for i in range(43, 52):
        # Check if the current element is a negative integer
        if my_list[i] < 0:
            # Add the current element to the list of negative integers
            neg_ints.append(my_list[i])
    # Return the list of all negative integers from index 43 to index 51, both inclusive
    return neg_ints
