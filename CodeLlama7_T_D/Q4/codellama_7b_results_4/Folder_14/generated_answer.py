
def all_pos_ints_exclusive(my_list):
    # Initialize an empty list to store the positive integers
    pos_ints = []
    # Iterate over the list of integers
    for i in range(len(my_list)):
        # Check if the current integer is positive and not equal to 0
        if my_list[i] > 0 and my_list[i] != 0:
            # Add the positive integer to the list of positive integers
            pos_ints.append(my_list[i])
    return pos_ints
