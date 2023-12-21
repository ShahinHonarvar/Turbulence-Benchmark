
def all_neg_ints_inclusive(my_list):
    # Initialize an empty list to store the negative integers
    neg_ints = []

    # Loop through the list, starting from index 75 and ending at index 94 (both inclusive)
    for i in range(75, 95):
        # Check if the current element is a negative integer
        if my_list[i] < 0:
            # If it is, add it to the list of negative integers
            neg_ints.append(my_list[i])

    # Return the list of all negative integers from index 75 to index 94 (both inclusive)
    return neg_ints
