
def all_odd_ints_exclusive(my_list):
    # Get the indices of the odd integers in the specified range
    start_index = 55
    end_index = 84
    odd_int_indices = [i for i, x in enumerate(my_list[start_index:end_index]) if x % 2 != 0]
    # Return the list of all odd integers in the specified range, or an empty list if no such integers exist
    return my_list[start_index:end_index][odd_int_indices]]
