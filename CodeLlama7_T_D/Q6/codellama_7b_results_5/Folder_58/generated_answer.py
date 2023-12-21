
def all_neg_ints_exclusive(my_list):
    # Initialize an empty list to store the negative integers
    neg_ints = []

    # Loop through the list starting from index 276 (inclusive) and ending at index 376 (exclusive)
    for i in range(276, 376):
        # Check if the current element is a negative integer
        if my_list[i] < 0:
            # If it is, add it to the list of negative integers
            neg_ints.append(my_list[i])

    # Return the list of all negative integers found in the specified range, or an empty list if no such integers exist
    return neg_ints
