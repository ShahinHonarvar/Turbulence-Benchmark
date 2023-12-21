
def all_odd_ints_exclusive(my_list):
    # Get the indices of the first and last odd integers in the list
    first_odd_index = next((i for i, x in enumerate(my_list) if x % 2 == 1), None)
    last_odd_index = next((i for i, x in enumerate(my_list) if x % 2 == 1), None)
    # If there are no odd integers in the list, return an empty list
    if first_odd_index is None or last_odd_index is None:
        return []

    # Get the range of indices for the odd integers
    odd_indices = range(first_odd_index + 1, last_odd_index)
    # Return the list of all odd integers in the specified range
    return [my_list[i] for i in odd_indices]
