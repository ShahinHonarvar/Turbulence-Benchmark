
def all_neg_ints_inclusive(my_list):
    # Initialize an empty list to store the negative integers
    neg_ints = []
    # Iterate through the list from index 28 to index 38, both inclusive
    for i in range(28, 39):
        # Check if the current element is a negative integer
        if my_list[i] < 0:
            # If it is a negative integer, add it to the list of negative integers
            neg_ints.append(my_list[i])
    # Return the list of all negative integers from index 28 to index 38, both inclusive
    return neg_ints
