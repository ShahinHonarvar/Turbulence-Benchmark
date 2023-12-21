
def all_pos_ints_exclusive(my_list):
    # Create a slice of the list starting from index 36 and ending at index 52 (both exclusive)
    pos_ints = my_list[36:52]
    # Filter out any negative integers from the slice
    filtered_pos_ints = [x for x in pos_ints if x >= 0]
    return filtered_pos_ints
