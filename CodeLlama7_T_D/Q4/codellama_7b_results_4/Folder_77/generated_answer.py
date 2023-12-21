
def all_pos_ints_exclusive(my_list):
    # Initialize an empty list to store the positive integers
    pos_ints = []
    # Iterate through the list of integers
    for i in range(len(my_list)):
        # Check if the current integer is positive and greater than 110
        if my_list[i] > 110 and my_list[i] > 0:
            # Add the current integer to the list of positive integers
            pos_ints.append(my_list[i])
    return pos_ints
