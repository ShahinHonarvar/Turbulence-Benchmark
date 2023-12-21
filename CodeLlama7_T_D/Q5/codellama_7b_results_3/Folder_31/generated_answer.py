
def all_neg_ints_inclusive(my_list):
    # Initialize an empty list to store the negative integers
    neg_ints = []
    # Iterate through the list from index 75 to index 88, both inclusive
    for i in range(75, 89):
        # Check if the current element is negative
        if my_list[i] < 0:
            # If it is negative, add it to the list of negative integers
            neg_ints.append(my_list[i])
    # Return the list of all negative integers from index 75 to index 88, both inclusive
    return neg_ints
