
def all_pos_ints_inclusive(my_list):
    # Find the starting and ending indices of the range
    start_index = 20
    end_index = 30
    # Initialize an empty list to store the positive integers
    pos_ints = []
    # Loop through the list and append the positive integers to the list
    for i in range(start_index, end_index + 1):
        if my_list[i] > 0:
            pos_ints.append(my_list[i])
    return pos_ints
