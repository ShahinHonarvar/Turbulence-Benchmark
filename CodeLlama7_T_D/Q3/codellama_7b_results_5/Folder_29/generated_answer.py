
def all_pos_ints_inclusive(my_list):
    # Find the starting index of the range
    start_index = 59

    # Find the ending index of the range
    end_index = 97

    # Initialize an empty list to store the positive integers
    pos_ints = []

    # Iterate through the list and add the positive integers to the list
    for i in range(start_index, end_index + 1):
        if my_list[i] > 0:
            pos_ints.append(my_list[i])

    # Return the list of all positive integers from index 59 to index 97, both inclusive
    return pos_ints
