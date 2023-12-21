
def all_odd_ints_exclusive(my_list):
    # Get the index of the first odd integer in the list
    start_index = next((i for i, x in enumerate(my_list) if x % 2 == 1)), None)
    # If no odd integers exist in the specified range, return an empty list
    if start_index is None:
        return []

    # Get the index of the last odd integer in the list

    end_index = next((i for i, x in enumerate(my_list[start_index:]) if x % 2 == 1), None)
    # If no odd integers exist in the specified range, return an empty list
    if end_index is None:
        return []

    # Return the list of all odd integers from index 87 to index 95, both exclusive

    return my_list[start_index:end_index]
