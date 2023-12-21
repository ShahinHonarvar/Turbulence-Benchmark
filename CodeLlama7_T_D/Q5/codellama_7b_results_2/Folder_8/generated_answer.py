
def all_neg_ints_inclusive(my_list):
    # Initialize an empty list to store the negative integers
    neg_ints = []

    # Iterate through the list starting from index 23
    for i in range(23, len(my_list)):
        # Check if the current element is negative
        if my_list[i] < 0:
            # If it is, add it to the list of negative integers
            neg_ints.append(my_list[i])

    # Return the list of all negative integers from index 23 to index 23, both inclusive
    return neg_ints
