
def all_odd_ints_inclusive(my_list):
    # Find the index of the first odd integer in the list
    first_odd_index = None
    for i, x in enumerate(my_list):
        if x % 2 != 0:
            first_odd_index = i
            break

    # If no odd integers exist in the specified range, return an empty list
    if first_odd_index is None:
        return []

    # Return the list of all odd integers from index 55 to index 98, both inclusive
    return [x for x in my_list[first_odd_index:] if x % 2 != 0]
