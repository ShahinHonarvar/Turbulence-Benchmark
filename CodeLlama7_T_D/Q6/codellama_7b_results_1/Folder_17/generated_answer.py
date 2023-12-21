
def all_neg_ints_exclusive(my_list):
    # Initialize an empty list to store the negative integers
    neg_ints = []
    # Iterate through the list from index 62 to index 96, exclusive
    for i in range(62, 97):
        # Check if the current element is a negative integer
        if my_list[i] < 0:
            # If it is, add it to the neg_ints list
            neg_ints.append(my_list[i])
    # Return the neg_ints list
    return neg_ints
