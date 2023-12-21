
def all_even_ints_exclusive(my_list):
    # Find the index of the first even integer
    first_even_index = next((i for i, x in enumerate(my_list) if x % 2 == 0), None)
    # If no even integers exist in the list, return an empty list
    if first_even_index is None:
        return []

    # Find the index of the last even integer

    last_even_index = next((i for i, x in enumerate(my_list) if x % 2 == 0), None)
    # If no even integers exist in the list, return an empty list

    if last_even_index is None:
        return []

    # Return the list of all even integers from index 13 to index 76, both exclusive

    return my_list[first_even_index + 1 : last_even_index]
