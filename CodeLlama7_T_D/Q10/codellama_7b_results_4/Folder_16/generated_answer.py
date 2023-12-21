
def all_odd_ints_exclusive(my_list):
    # Get the range of indices for odd integers
    start_index = next((i for i, x in enumerate(my_list) if x % 2 == 1), None)
    end_index = next((i for i, x in enumerate(my_list[start_index:]) if x % 2 == 1), None)
    # Return an empty list if no odd integers exist in the specified range
    if start_index is None or end_index is None:
        return []

    # Return the list of all odd integers from index 86 to index 90, both exclusive
    else:
        return my_list[start_index:end_index]
