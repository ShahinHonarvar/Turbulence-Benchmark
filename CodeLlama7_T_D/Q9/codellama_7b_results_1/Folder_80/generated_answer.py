
def all_odd_ints_inclusive(my_list):
    # Find the index of the first odd integer
    first_odd_index = None
    for i in range(64, 67):
        if my_list[i] % 2 != 0:
            first_odd_index = i
            break

    # If no odd integers exist in the specified range, return an empty list
    if first_odd_index is None:
        return []

    # Return the list of all odd integers from index 64 to index 66, both inclusive
    return [my_list[i] for i in range(first_odd_index, first_odd_index + 3)]
