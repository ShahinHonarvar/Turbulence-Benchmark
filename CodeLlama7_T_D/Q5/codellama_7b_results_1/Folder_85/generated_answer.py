
def all_neg_ints_inclusive(my_list):
    # Initialize an empty list to store the negative integers
    neg_ints = []
    # Loop through the list starting from index 6 (inclusive)
    for i in range(6, len(my_list)):
        # Check if the current element is a negative integer
        if my_list[i] < 0:
            # If it is, add it to the neg_ints list
            neg_ints.append(my_list[i])
    # Return the neg_ints list
    return neg_ints
