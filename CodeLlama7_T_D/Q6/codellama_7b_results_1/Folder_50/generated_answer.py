
def all_neg_ints_exclusive(my_list):
    # Initialize an empty list to store the negative integers
    neg_ints = []
    # Iterate over the list of integers starting from index 70 (inclusive) and ending at index 98 (exclusive)
    for i in range(70, 98):
        # Check if the current element is a negative integer
        if my_list[i] < 0:
            # If it is a negative integer, add it to the list of negative integers
            neg_ints.append(my_list[i])
    # Return the list of all negative integers in the specified range
    return neg_ints
