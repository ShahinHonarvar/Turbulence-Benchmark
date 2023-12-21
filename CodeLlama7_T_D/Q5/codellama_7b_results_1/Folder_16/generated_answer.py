
def all_neg_ints_inclusive(my_list):
    # Initialize an empty list to store the negative integers
    neg_ints = []
    # Loop through the list and check if each element is negative
    for i in range(33, 36 + 1):
        if my_list[i] < 0:
            # If the element is negative, add it to the list of negative integers
            neg_ints.append(my_list[i])
    # Return the list of all negative integers from index 33 to index 36, both inclusive
    return neg_ints
