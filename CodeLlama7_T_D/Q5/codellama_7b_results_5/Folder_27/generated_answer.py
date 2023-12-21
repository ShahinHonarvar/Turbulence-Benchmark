
def all_neg_ints_inclusive(my_list):
    # Initialize an empty list to store the negative integers
    neg_ints = []
    # Loop through the list from index 66 to index 93, both inclusive
    for i in range(66, 94):
        # If the current element is a negative integer, add it to the neg_ints list
        if my_list[i] < 0:
            neg_ints.append(my_list[i])
    # Return the list of all negative integers from index 66 to index 93, both inclusive
    return neg_ints
