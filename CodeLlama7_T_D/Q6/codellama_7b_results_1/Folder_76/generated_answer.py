
def all_neg_ints_exclusive(my_list):
    # Find the starting and ending indices of the negative integers in the list
    start_index = my_list[361:].index(-1) + 361
    end_index = my_list[start_index:].index(-1) + start_index
    # Return the list of all negative integers from index 361 to index 643, both exclusive
    return my_list[start_index:end_index]
