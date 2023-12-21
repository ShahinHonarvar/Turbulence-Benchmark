
def all_pos_ints_exclusive(my_list):
    # Initialize an empty list to store the positive integers
    pos_ints = []
    # Loop through the list of integers starting from index 56 (inclusive) and ending at index 88 (exclusive)
    for i in range(56, 88):
        # If the current element is a positive integer, append it to the pos_ints list
        if my_list[i] > 0:
            pos_ints.append(my_list[i])
    return pos_ints
