
def all_even_ints_exclusive(my_list):
    # Find the index of the first even integer in the list
    first_even_index = next((i for i, x in enumerate(my_list) if x % 2 == 0), None)
    # If there are no even integers in the list, return an empty list
    if first_even_index is None:
        return []

    # Find the index of the last even integer in the list
    last_even_index = next((i for i in range(first_even_index, len(my_list))), None)
    # If there are no even integers in the specified range, return an empty list
    if last_even_index is None:
        return []

    # Return a list of all even integers from index 80 to index 200, both exclusive
    return [my_list[i] for i in range(first_even_index, last_even_index)]
