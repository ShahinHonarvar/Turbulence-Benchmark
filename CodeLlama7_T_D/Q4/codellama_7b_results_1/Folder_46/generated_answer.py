
def all_pos_ints_exclusive(my_list):
    # Get the length of the list
    list_len = len(my_list)
    # Initialize an empty list to store the positive integers
    pos_ints = []
    # Iterate over the list from index 20 to 43, exclusive
    for i in range(20, list_len):
        # Check if the current element is a positive integer
        if my_list[i] > 0:
            # If it is, add it to the list of positive integers
            pos_ints.append(my_list[i])
    return pos_ints
