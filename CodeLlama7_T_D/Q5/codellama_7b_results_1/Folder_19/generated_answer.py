
def all_neg_ints_inclusive(my_list):
    # Initialize an empty list to store the negative integers
    neg_ints = []

    # Iterate through the list from index 3 to index 5, both inclusive
    for i in range(3, 6):

        # If the current element is a negative integer, append it to the list of negative integers
        if my_list[i] < 0:
            neg_ints.append(my_list[i])

    # Return the list of negative integers
    return neg_ints
