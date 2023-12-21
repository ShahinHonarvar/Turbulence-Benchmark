
def all_neg_ints_exclusive(my_list):
    # Initialize an empty list to store the negative integers
    neg_ints = []

    # Iterate through the list of integers, starting from index 64 and ending at index 80 (both exclusive)
    for i in range(64, 81):

        # If the current element is negative, add it to the list of negative integers
        if my_list[i] < 0:
            neg_ints.append(my_list[i])

    # Return the list of negative integers
    return neg_ints
