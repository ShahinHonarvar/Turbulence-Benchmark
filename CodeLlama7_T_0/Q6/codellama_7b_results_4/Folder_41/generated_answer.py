
def all_neg_ints_exclusive(my_list):
    # Initialize an empty list to store the negative integers
    neg_ints = []

    # Iterate through the list and check if each element is a negative integer
    for i in range(8, 10):
        if my_list[i] < 0:
            # If the element is a negative integer, add it to the list of negative integers
            neg_ints.append(my_list[i])

    # Return the list of all negative integers from index 8 to index 9, both exclusive
    return neg_ints
