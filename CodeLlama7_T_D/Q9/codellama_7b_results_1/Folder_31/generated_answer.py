
def all_odd_ints_inclusive(my_list):
    # Get the indices of the first and last odd integers in the list
    first_odd_index = next((i for i, x in enumerate(my_list) if x % 2 == 1), None)
    last_odd_index = next((i for i, x in enumerate(my_list[::-1]) if x % 2 == 1), None)
    # If there are no odd integers in the list, return an empty list
    if first_odd_index is None or last_odd_index is None:
        return []

    # Return the list of all odd integers from index 75 to index 88, both inclusive
    return my_list[first_odd_index:last_odd_index+1]
