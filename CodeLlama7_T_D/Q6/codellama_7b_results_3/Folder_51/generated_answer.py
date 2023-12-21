
def all_neg_ints_exclusive(my_list):
    # Initialize an empty list to store the negative integers
    neg_ints = []
    # Iterate through the list from index 6 to index 9 (both exclusive)
    for i in range(5, 10):
        # If the current element is a negative integer, add it to the list of negative integers
        if my_list[i] < 0:
            neg_ints.append(my_list[i])
    # Return the list of negative integers
    return neg_ints
