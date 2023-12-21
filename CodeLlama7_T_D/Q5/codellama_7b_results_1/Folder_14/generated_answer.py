
def all_neg_ints_inclusive(my_list):
    # Initialize an empty list to store the negative integers
    neg_ints = []

    # Iterate through the list from index 5 to index 7, both inclusive
    for i in range(5, 8):

        # If the current element is a negative integer, append it to the neg_ints list
        if my_list[i] < 0:
            neg_ints.append(my_list[i])

    # Return the list of all negative integers from index 5 to index 7, both inclusive
    return neg_ints
