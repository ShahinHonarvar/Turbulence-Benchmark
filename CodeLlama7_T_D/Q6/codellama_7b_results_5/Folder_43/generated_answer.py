
def all_neg_ints_exclusive(my_list):
    # Initialize an empty list to store the negative integers
    neg_ints = []

    # Iterate through the list starting from index 38 (inclusive) and ending at index 77 (exclusive)
    for i in range(38, 77):
        # Check if the current element is a negative integer
        if my_list[i] < 0:
            # If it is, add it to the list of negative integers
            neg_ints.append(my_list[i])

    # Return the list of all negative integers from index 38 to index 77 (exclusive)
    return neg_ints
