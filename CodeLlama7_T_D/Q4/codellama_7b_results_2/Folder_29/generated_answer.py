
def all_pos_ints_exclusive(my_list):
    # Get the length of the list
    list_length = len(my_list)
    # Initialize an empty list to store the positive integers
    pos_ints = []
    # Loop through the indices of the list from 48 to 76, both exclusive
    for i in range(48, list_length):
        # Check if the current index has a positive integer value
        if my_list[i] > 0:
            # If it does, add it to the list of positive integers
            pos_ints.append(my_list[i])
    # Return the list of all positive integers from index 48 to index 76, both exclusive
    return pos_ints
