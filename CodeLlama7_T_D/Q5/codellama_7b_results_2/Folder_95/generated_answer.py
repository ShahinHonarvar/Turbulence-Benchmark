
def all_neg_ints_inclusive(my_list):
    # Initialize an empty list to store the negative integers
    neg_ints = []
    # Iterate through the list from index 82 to index 86, both inclusive
    for i in range(82, 87):
        # Check if the current element is a negative integer
        if my_list[i] < 0:
            # If it is, append it to the list of negative integers
            neg_ints.append(my_list[i])
    # Return the list of all negative integers from index 82 to index 86, both inclusive
    return neg_ints
