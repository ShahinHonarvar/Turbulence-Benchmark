
def all_neg_ints_exclusive(my_list):
    # Initialize an empty list to store the negative integers
    neg_ints = []
    # Loop through the list of integers starting from index 369 (inclusive) and ending at index 983 (exclusive)
    for i in range(369, 983):
        # If the current element is negative, append it to the neg_ints list
        if my_list[i] < 0:
            neg_ints.append(my_list[i])
    # Return the neg_ints list
    return neg_ints
