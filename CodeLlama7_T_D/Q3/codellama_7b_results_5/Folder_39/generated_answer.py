
def all_pos_ints_inclusive(my_list):
    # find the starting index of the range
    start_index = 20

    # find the ending index of the range
    end_index = 30

    # initialize an empty list to store the positive integers
    pos_ints = []

    # loop through the list from the starting index to the ending index
    for i in range(start_index, end_index + 1):
        # check if the current element is a positive integer
        if my_list[i] > 0:
            # add the positive integer to the list of positive integers
            pos_ints.append(my_list[i])

    # return the list of positive integers
    return pos_ints
