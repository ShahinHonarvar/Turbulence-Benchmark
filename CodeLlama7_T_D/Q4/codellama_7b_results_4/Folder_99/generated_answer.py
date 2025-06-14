
def all_pos_ints_exclusive(my_list):
    # Initialize an empty list to store the positive integers
    pos_ints = []
    # Loop through the list and check if each element is a positive integer
    for i in range(295, 574):
        if my_list[i] > 0:
            # If the element is a positive integer, add it to the list of positive integers
            pos_ints.append(my_list[i])
    # Return the list of all positive integers from index 295 to index 573, both exclusive
    return pos_ints
