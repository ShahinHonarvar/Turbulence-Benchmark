
def all_pos_ints_inclusive(my_list):
    # Create a new list to store the positive integers
    pos_ints = []
    # Loop through the list of integers
    for i in range(len(my_list)):
        # Check if the current integer is positive
        if my_list[i] > 0:
            # Add the positive integer to the new list
            pos_ints.append(my_list[i])
    return pos_ints
