
def all_pos_ints_inclusive(my_list):
    # Initialize an empty list to store the positive integers
    pos_ints = []
    # Iterate through the list of integers
    for i in range(len(my_list)):
        # Check if the current integer is positive and add it to the list of positive integers
        if my_list[i] > 0:
            pos_ints.append(my_list[i])
    return pos_ints
