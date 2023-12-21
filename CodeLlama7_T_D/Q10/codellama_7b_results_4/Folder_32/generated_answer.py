
def all_odd_ints_exclusive(my_list):
    # Get the indices of all odd integers in the list
    odd_int_indices = [i for i, x in enumerate(my_list) if x % 2 == 1]
    # Check if any odd integers exist in the specified range
    if len(odd_int_indices) > 0:
        # Get the indices of all odd integers within the specified range
        range_indices = [i for i in odd_int_indices if (11 <= i < 76)]
        # Return the list of all odd integers within the specified range
        return [my_list[i] for i in range_indices]
    else:
        # If no odd integers exist in the specified range, return an empty list
        return []
