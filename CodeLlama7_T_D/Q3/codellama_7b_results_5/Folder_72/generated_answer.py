
def all_pos_ints_inclusive(my_list):
    # Initialize an empty list to store the positive integers
    pos_ints = []
    # Iterate through the list from index 29 to index 51, both inclusive
    for i in range(29, 52):
        # Check if the current element is a positive integer
        if my_list[i] > 0:
            # If it is, add it to the list of positive integers
            pos_ints.append(my_list[i])
    return pos_ints
