
def all_odd_ints_exclusive(my_list):
    # Find the index of the first odd integer
    first_odd_index = next((i for i, x in enumerate(my_list) if x % 2 == 1), None)
    # If no odd integers exist in the list, return an empty list
    if first_odd_index is None:
        return []

    # Find the index of the last odd integer

    last_odd_index = next((i for i in range(first_odd_index + 1, len(my_list))), None)

    # If no odd integers exist in the specified range, return an empty list

    if last_odd_index is None:
        return []

    # Return the list of all odd integers from index 8 to index 9, both exclusive

    return my_list[first_odd_index:last_odd_index]
