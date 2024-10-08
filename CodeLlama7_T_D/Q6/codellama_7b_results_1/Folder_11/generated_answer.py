
def all_neg_ints_exclusive(my_list):
    # Initialize an empty list to store the negative integers
    neg_ints = []
    # Iterate through the list of integers starting from index 15 (inclusive) and ending at index 99 (exclusive)
    for i in range(15, 99):
        # Check if the current element is a negative integer
        if my_list[i] < 0:
            # If it is a negative integer, add it to the list of negative integers
            neg_ints.append(my_list[i])
    # Return the list of all negative integers from index 15 to index 99 (exclusive)
    return neg_ints
