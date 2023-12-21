
def all_neg_ints_exclusive(my_list):
    # Initialize an empty list to store the negative integers
    neg_ints = []
    # Loop through the list from index 59 to index 93, both exclusive
    for i in range(59, 94):
        # If the current element is a negative integer, add it to the list of negative integers
        if my_list[i] < 0:
            neg_ints.append(my_list[i])
    # Return the list of all negative integers from index 59 to index 93, both exclusive
    return neg_ints
