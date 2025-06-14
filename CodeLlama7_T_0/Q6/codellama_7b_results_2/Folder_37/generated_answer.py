
def all_neg_ints_exclusive(my_list):
    # Initialize an empty list to store the negative integers
    neg_ints = []

    # Iterate through the list and check if each element is a negative integer
    for i in range(1, len(my_list)):
        if my_list[i] < 0:
            neg_ints.append(my_list[i])

    # Return the list of all negative integers from index 1 to index 2, both exclusive
    return neg_ints
