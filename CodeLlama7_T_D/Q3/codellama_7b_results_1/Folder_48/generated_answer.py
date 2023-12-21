
def all_pos_ints_inclusive(my_list):
    # Create a new list to store the positive integers
    pos_ints = []
    # Loop through the specified range of indices in the input list
    for i in range(533, 605 + 1):
        # Check if the current element is a positive integer
        if my_list[i] > 0:
            # If it is, add it to the new list
            pos_ints.append(my_list[i])
    return pos_ints
