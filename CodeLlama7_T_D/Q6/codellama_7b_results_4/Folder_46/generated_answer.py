
def all_neg_ints_exclusive(my_list):
    # Initialize an empty list to store the negative integers
    neg_ints = []

    # Iterate through the list, starting from index 20 (inclusive) and ending at index 43 (exclusive)
    for i in range(20, 43):

        # Check if the current element is negative

        if my_list[i] < 0:

            # If it is negative, append it to the list of negative integers

            neg_ints.append(my_list[i])

    # Return the list of all negative integers from index 20 to index 43 (exclusive)

    return neg_ints
