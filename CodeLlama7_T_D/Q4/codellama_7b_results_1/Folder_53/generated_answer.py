
def all_pos_ints_exclusive(my_list):
    # Initialize an empty list to store the positive integers
    pos_ints = []
    # Iterate through the list of integers
    for i in range(100, 200):
        # If the current element is a positive integer, append it to the list of positive integers
        if my_list[i] > 0:
            pos_ints.append(my_list[i])
    return pos_ints
