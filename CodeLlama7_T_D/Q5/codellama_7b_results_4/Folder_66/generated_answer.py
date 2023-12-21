
def all_neg_ints_inclusive(my_list):
    # Initialize an empty list to store the negative integers
    neg_ints = []

    # Iterate through the list from index 50 to index 54, both inclusive
    for i in range(50, 55):
        # Check if the current element is a negative integer
        if my_list[i] < 0:
            # Add the negative integer to the list of negative integers
            neg_ints.append(my_list[i])

    # Return the list of negative integers
    return neg_ints
