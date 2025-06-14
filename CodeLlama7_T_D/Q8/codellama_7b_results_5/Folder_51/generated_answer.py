
def all_even_ints_exclusive(my_list):
    # Find the index of the first even integer in the list
    first_even_index = next((i for i, x in enumerate(my_list) if x % 2 == 0), None)
    # If no even integers exist in the specified range, return an empty list
    if first_even_index is None:
        return []

    # Find the index of the last even integer in the list

    last_even_index = next((i for i, x in enumerate(my_list[first_even_index:]) if x % 2 == 0), None)
    # If no even integers exist in the specified range, return an empty list
    if last_even_index is None:
        return []

    # Return the list of all even integers from index 6 to index 9, both exclusive

    return my_list[first_even_index:first_even_index + 6] + my_list[last_even_index - 3:last_even_index + 1]
