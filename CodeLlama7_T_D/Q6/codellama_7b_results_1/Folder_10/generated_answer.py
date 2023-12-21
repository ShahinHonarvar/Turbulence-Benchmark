
def all_neg_ints_exclusive(my_list):
    # Initialize an empty list to store the negative integers
    neg_ints = []

    # Loop through the list and check if each element is a negative integer
    for i in range(48, 75):
        if my_list[i] < 0:
            neg_ints.append(my_list[i])

    # Return the list of all negative integers from index 48 to index 74, both exclusive
    return neg_ints
