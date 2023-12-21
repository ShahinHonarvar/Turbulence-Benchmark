
def all_even_ints_inclusive(my_list):
    # Find the index of the first even integer
    first_even_index = next((i for i, x in enumerate(my_list) if x % 2 == 0), None)
    # If no even integers exist in the list, return an empty list
    if first_even_index is None:
        return []

    # Find the index of the last even integer

    last_even_index = next(i for i, x in enumerate(my_list[first_even_index:]) if x % 2 == 0), None)
    # If no even integers exist in the specified range, return an empty list
    if last_even_index is None:
        return []

    # Return the list of all even integers from index 56 to index 66, both inclusive
    return my_list[first_even_index:last_even_index+1]
