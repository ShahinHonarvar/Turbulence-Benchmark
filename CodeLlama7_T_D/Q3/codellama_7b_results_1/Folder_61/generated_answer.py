
def all_pos_ints_inclusive(my_list):
    # Initialize an empty list to store the positive integers
    pos_ints = []
    # Loop through the list of integers
    for i in range(len(my_list)):
        # If the current element is a positive integer, append it to the list of positive integers
        if my_list[i] > 0:
            pos_ints.append(my_list[i])
    # Return the list of all positive integers from index 0 to index 7, both inclusive
    return pos_ints
